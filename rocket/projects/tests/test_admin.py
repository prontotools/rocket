from django.contrib import admin
from django.test import TestCase

from ..admin import (
    ProjectAdmin,
    ProjectGroupAdmin,
)
from ..models import (
    Project,
    ProjectGroup,
)


class ProjectAdminTest(TestCase):
    def test_project_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[Project],
            ProjectAdmin
        )

    def test_project_admin_should_set_list_display(self):
        expected = (
            'name',
            'slug',
            'description',
            'project_group',
            'token',
        )
        self.assertEqual(ProjectAdmin.list_display, expected)

    def test_project_admin_should_set_list_filter(self):
        expected = (
            'project_group',
        )
        self.assertEqual(ProjectAdmin.list_filter, expected)


class ProjectGroupAdminTest(TestCase):
    def test_project_group_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[ProjectGroup],
            ProjectGroupAdmin
        )

    def test_project_group_admin_should_set_list_display(self):
        expected = (
            'name',
            'slug',
            'description',
        )
        self.assertEqual(ProjectGroupAdmin.list_display, expected)
