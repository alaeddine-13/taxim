from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

import base64
import json

PASSWORD = 'pAssw0rd!'

def create_user(username='user', password=PASSWORD):
    return get_user_model().objects.create_user(
        username=username,
        first_name='Test',
        last_name='User',
        password=password,
        email="user@example.com",
        is_superuser=True
    )


def create_application_client(user):
    return Application.objects.create(
        user=user,
        client_type="Confidential",
        authorization_grant_type="Resource owner password-based")

class AuthenticationTest(APITestCase):
    def test_user_can_signup(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'user',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': PASSWORD,
            'password2': PASSWORD,
            'email': 'user@example.com'
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
    
    def test_user_can_login(self):
        user = create_user()
        response = self.client.post(reverse('login'), data={
            'username': user.username,
            'password': PASSWORD,
        })

        # Parse payload data from access token.
        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(payload_data['id'], user.id)
        self.assertEqual(payload_data['username'], user.username)
        self.assertEqual(payload_data['first_name'], user.first_name)
        self.assertEqual(payload_data['last_name'], user.last_name)
