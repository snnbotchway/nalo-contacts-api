
from . import views
from django.urls import path

app_name= 'api'

urlpatterns = [
    path('contact-list', views.contactList, name='list'),
    path('<int:pk>', views.contactDetail, name='detail'),
    path('contact-create', views.contactCreate, name='create'),
    path('contact-edit/<int:pk>', views.contactEdit, name='edit'),
    path('contact-delete/<int:pk>', views.contactDelete, name='delete'),
    path('upload-csv/', views.uploadCsv, name='upload-csv'),
]