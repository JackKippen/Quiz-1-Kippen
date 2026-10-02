from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import TechStack


class AdminAuthTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.superuser = self.user_model.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='StrongPass!123',
        )
        self.regular_user = self.user_model.objects.create_user(
            username='regular',
            email='regular@example.com',
            password='StrongPass!123',
        )

    def test_superuser_can_login_and_access_dashboard(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'admin', 'password': 'StrongPass!123'},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertContains(response, 'Dashboard')

    def test_regular_user_cannot_login_to_admin_login_page(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'regular', 'password': 'StrongPass!123'},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Only superusers may sign in here')

    def test_dashboard_requires_superuser(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

        self.client.login(username='regular', password='StrongPass!123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_superuser_can_create_project_with_tech_stack(self):
        self.client.login(username='admin', password='StrongPass!123')
        TechStack.objects.create(name='Python')

        response = self.client.post(
            reverse('dashboard_project_create'),
            {
                'project_name': 'Portfolio Site',
                'description': 'A full portfolio project built in Django.',
                'tech_stacks': '1',
                'link': 'https://example.com',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Portfolio Site')
