from django.contrib import admin
from django.test import TestCase

from ..admin import EnvironmentAdmin
from ..models import Environment


class EnvironmentAdminTest(TestCase):
    def test_environment_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[Environment],
            EnvironmentAdmin
        )

    def test_environment_admin_should_set_list_display(self):
        expected = (
            'name',
            'project',
            'branch',
        )
        self.assertEqual(EnvironmentAdmin.list_display, expected)

    def test_environment_admin_should_set_list_filter(self):
        expected = (
            'project',
        )
        self.assertEqual(EnvironmentAdmin.list_filter, expected)
