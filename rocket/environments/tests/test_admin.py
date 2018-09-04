from django.contrib.auth.models import User
from django.test import TestCase

from ..admin import EnvironmentAdmin


class EnvironmentAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='admin',
            password='123',
            email=''
        )
        self.client.login(
            username='admin',
            password='123'
        )
        self.url = '/admin/environments/environment/'

    def test_access_environment_admin_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_environment_admin_should_set_list_display(self):
        expected = (
            'name',
        )
        self.assertEqual(EnvironmentAdmin.list_display, expected)
