from django.contrib.auth.models import User
from django.test import TestCase

from ..admin import (
    ProjectAdmin,
    ProjectGroupAdmin,
)


class ProjectAdminTest(TestCase):
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
        self.url = '/admin/projects/project/'

    def test_access_project_admin_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

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
        self.url = '/admin/projects/projectgroup/'

    def test_access_project_group_admin_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_project_group_admin_should_set_list_display(self):
        expected = (
            'name',
            'slug',
            'description',
        )
        self.assertEqual(ProjectGroupAdmin.list_display, expected)
