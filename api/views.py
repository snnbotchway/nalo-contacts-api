from django.contrib import messages
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Contact
from api.serializers import ContactSerializer
import csv,io
from django.contrib.auth.decorators import permission_required

from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
@permission_required('admin.can_add_log_entry')
@api_view(['GET'])
def contactList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    contacts = Contact.objects.all()
    result_page = paginator.paginate_queryset(contacts, request)
    serializer = ContactSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@permission_required('admin.can_add_log_entry')
@api_view(['GET'])
def contactDetail(request, pk):
    contact = Contact.objects.get(id = pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)

@permission_required('admin.can_add_log_entry')
@api_view(['POST'])
def contactCreate(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('Invalid Data, name should not be more than 100 characters and phone should not be more than 10 characters')

@permission_required('admin.can_add_log_entry')
@api_view(['POST'])
def contactEdit(request, pk):
    contact = Contact.objects.get(id = pk)
    serializer = ContactSerializer(instance=contact, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('Invalid Data, name should not be more than 100 characters and phone should not be more than 10 characters')

@permission_required('admin.can_add_log_entry')
@api_view(['DELETE'])
def contactDelete(request, pk):
    contact = Contact.objects.get(id = pk)
    contact.delete()
    return Response('Deletion Successful')

@permission_required('admin.can_add_log_entry')
def uploadCsv(request):
    template = 'upload-csv.html'

    prompt = {
        'order': 'Order of CSV should be name, phone'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    contact_list = []
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        contact = Contact(
            name = column[0],
            phone = column[1]
        )

        contact_list.append(contact)
    
    Contact.objects.bulk_create(contact_list)
    if contact_list:
        send_mail(
            'CSV file uploaded',
            'Your csv file was uploaded and the database was successfully populated with the information',
            'solomonbotchway7@gmail.com',
            [request.user.email],
            fail_silently=False,
        )
        print('email sent')
        print(request.user.email)
    contact_list = []

    context= {}

    return render(request, template, context)

    



# def uploadCsv(request):
#     data = {}
#     if "GET" == request.method:
#         return render(request, "upload-csv.html", data)
#     # if not GET, then proceed with processing
#     try:
#         csv_file = request.FILES["csv_file"]
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return HttpResponseRedirect(reverse("api:upload-csv"))
#         #if file is too large, return message
#         if csv_file.multiple_chunks():
#             messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#             return HttpResponseRedirect(reverse("api:upload-csv"))
#         file_data = csv_file.read().decode("utf-8")          

#         lines = file_data.split("\n")
#         #loop over the lines and save them in db. If error shows up , store as string and then display
#         for line in lines:                                          
#             fields = line.split(",")
#             data_dict = {}
#             data_dict["name"] = fields.first()
#             data_dict["phone"] = fields[1]
#         try:
#             form = EventsForm(data_dict)
#             if form.is_valid():
#                 form.save()                                  
#             else:
#                 logging.getLogger("error_logger").error(form.errors.as_json())                                                                                    
#         except Exception as e:
#             logging.getLogger("error_logger").error(repr(e))                             
#             pass

#     except Exception as e:
#         logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#         messages.error(request,"Unable to upload CVS file. "+repr(e))

#         return HttpResponseRedirect(reverse("api:upload-csv"))
