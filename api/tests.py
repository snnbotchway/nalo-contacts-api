from django.urls import reverse, resolve 
from rest_framework.test import APITestCase
from rest_framework import status
from api.serializers import ContactSerializer
from .models import Contact
from .views import contactList

# Create your tests here.

class CreateContactTest(APITestCase):

    def test_create_contact(self):
        data = {
            "name": "Solomon Botchway", 
            "phone":"0558447644"
        }
        response = self.client.post('/api/contact-create', data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class ListContactsTest(APITestCase):
    """ Test module for GET all contacts API """

    def setup(self):
        Contact.objects.create(
            name='Solomon Botchway', phone='0558447644')
        Contact.objects.create(
            name='Ivan Asamoah', phone='0249389232')
        Contact.objects.create(
            name='Priscilla Antwi', phone='0273450987')
        Contact.objects.create(
            name='Evaina Boamah', phone='0274567893')

    def test_list_contacts(self):
        response = self.client.get('/api/contact-list')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class ContactDetailTest(APITestCase):
    """ Test module for GET all contacts API """

    def setup(self):
        Contact.objects.create(
            name='Solomon Botchway', phone='0558447644')
        Contact.objects.create(
            name='Ivan Asamoah', phone='0249389232')

    def test_contact_detail(self):
        response = self.client.get('/api/1')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class ContactEditTest(APITestCase):
    """ Test module for GET all contacts API """

    def setup(self):
        Contact.objects.create(
            name='Solomon Botchway', phone='0558447644')
        Contact.objects.create(
            name='Ivan Asamoah', phone='0249389232')

    def test_contact_edit(self):
        data = {
            "name": "Solomon Botchway", 
            "phone":"0558447644"
        }
        response = self.client.post('/api/contact-edit/2', data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class ContactDeleteTest(APITestCase):
    """ Test module for GET all contacts API """

    def setup(self):
        Contact.objects.create(
            name='Solomon Botchway', phone='0558447644')
        Contact.objects.create(
            name='Ivan Asamoah', phone='0249389232')

    def test_contact_delete(self):
        data = {
            "name": "Solomon Botchway", 
            "phone":"0558447644"
        }
        response = self.client.post('/api/contact-delete/2', data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    

