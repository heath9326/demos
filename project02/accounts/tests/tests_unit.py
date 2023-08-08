from django.test import TestCase
#from django.core.urlresolvers import reverse
from rest_framework import status

from common.factories import RandomUserFactory
from accounts.models import CustomUser

# Create your tests here.

# class TestRandomUserFactory(TestCase):

#     def setUp(self):
#         # Create superuser and log them in:
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         #Create test users here:
#         self.users = RandomUserFactory.build_batch(10)


#     def test__can_get_user_list(self):
#     #     # Send a get request to the url
#         response = self.client.get(reverse('getusersapi'), self.data)
#     #     # Check if the response is OK
#         self.assertEqual(response.status_code, status.HTTP_200_OK)