from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import YourModel


# class YourModelTests(APITestCase):
#     def test_create_book(self):
#         data = {"field1": "value1", "field2": "value2"}
#         response = self.client.post("/yourmodel/", data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
