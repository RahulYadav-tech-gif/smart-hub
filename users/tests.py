from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='rahul', password='testpass123')

    def test_register_page_status(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'rahul', 'password': 'testpass123'})
        self.assertEqual(response.status_code, 302)  # redirect after login

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/users/login/?next=/users/dashboard/')
