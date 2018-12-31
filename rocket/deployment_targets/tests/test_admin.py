from django.contrib import admin
from django.test import TestCase

from ..admin import DeploymentTargetAdmin
from ..models import DeploymentTarget


class DeploymentTargetAdminTest(TestCase):
    def test_deployment_target_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[DeploymentTarget],
            DeploymentTargetAdmin
        )

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
