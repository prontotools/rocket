from django.test import TestCase

from ..models import Project, ProjectGroup


class ProjectTest(TestCase):
    def test_save_project(self):
        project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )

        project = Project()
        project.name = 'Pronto World'
        project.slug = 'pronto-world'
        description = 'Pronto World is the dashboard where Pronto ' \
            'clients can sign up for services, monitor website analytics, ' \
            'and manage their account.'
        project.description = description
        project.project_group = project_group
        project.save()

        project = Project.objects.last()

        self.assertEqual(project.name, 'Pronto World')
        self.assertEqual(project.slug, 'pronto-world')
        self.assertEqual(project.description, description)
        self.assertEqual(project.project_group.id, project_group.id)


class ProjectGroupTest(TestCase):
    def test_save_project_group(self):
        project_group = ProjectGroup()
        project_group.name = 'Pronto World'
        project_group.slug = 'pronto-world'
        project_group.description = 'Pronto World Group'
        project_group.save()

        project = Project.objects.last()

        self.assertEqual(project_group.name, 'Pronto World')
        self.assertEqual(project_group.slug, 'pronto-world')
        self.assertEqual(project_group.description, 'Pronto World Group')
