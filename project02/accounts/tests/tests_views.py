import unittest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from test_plus.test import (
                            CBVTestCase,
                            NoPreviousResponse,
                            TestCase,
                            APITestCase,
                            )

from test_plus.compat import DRF

from common.factories import RandomUserFactory
from accounts.models import CustomUser



# @unittest.skipUnless(DRF is True, 'DRF is not installed.')
# class TestGetCustomUsersView(APITestCase):

#     def test_



# Create your tests here.

class TestGetCustomUsersView(TestCase):

    def setUp(self):
        # Create superuser and log them in:
        self.superuser = CustomUser.objects.create_superuser('john', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        #Create test users here:
        self.users = RandomUserFactory.create_batch(10)
        self.users2 = RandomUserFactory.create_batch(10)


    def test__can_get_user_by_id(self):
    #     # Send a get request to the url
        # response = self.client.get(reverse('accounts:getusersapi'))
        response = self.get('/accounts/getusersapi', data={'id': self.users2[0].id})
        import json
        print(response.json())
    #     # Check if the response is OK
        self.response_200()
        # self.assertEqual(response.status_code, 200)