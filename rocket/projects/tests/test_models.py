from django.test import TestCase

from ..models import Project


class ProjectTest(TestCase):
    def test_save_project(self):
        project = Project()
        project.name = 'Pronto World'
        project.slug = 'pronto-world'
        description = 'Pronto World is the dashboard where Pronto ' \
            'clients can sign up for services, monitor website analytics, ' \
            'and manage their account.'
        project.description = description
        project.save()

        project = Project.objects.last()

        self.assertEqual(project.name, 'Pronto World')
        self.assertEqual(project.slug, 'pronto-world')
        self.assertEqual(project.description, description)
