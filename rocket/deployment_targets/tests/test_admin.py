from django.contrib.auth.models import User
from django.test import TestCase

from ..admin import DeploymentTargetAdmin


class DeploymentTargetAdminTest(TestCase):
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
        self.url = '/admin/deployment_targets/deploymenttarget/'

    def test_access_deployment_target_admin_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_deployment_target_admin_should_set_list_display(self):
        expected = (
            'name',
            'ip',
            'environment',
        )
        self.assertEqual(DeploymentTargetAdmin.list_display, expected)

    def test_deployment_target_admin_should_set_list_filter(self):
        expected = (
            'environment',
        )
        self.assertEqual(DeploymentTargetAdmin.list_filter, expected)
