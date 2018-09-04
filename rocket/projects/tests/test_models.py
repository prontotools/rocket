from django.test import TestCase

from ..models import (
    Project,
    ProjectGroup,
)


class ProjectTest(TestCase):
    def setUp(self):
        self.project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )

    def test_save_project(self):
        project = Project()
        project.name = 'Pronto World'
        project.slug = 'pronto-world'
        description = 'Pronto World is the dashboard where Pronto ' \
            'clients can sign up for services, monitor website analytics, ' \
            'and manage their account.'
        project.description = description
        project.project_group = self.project_group
        project.save()

        project = Project.objects.last()

        self.assertEqual(project.name, 'Pronto World')
        self.assertEqual(project.slug, 'pronto-world')
        self.assertEqual(project.description, description)
        self.assertEqual(project.project_group.id, self.project_group.id)

    def test_project_should_have_friendly_name(self):
        project = Project.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Description',
            project_group=self.project_group
        )
        self.assertEqual(project.__str__(), 'Pronto World')


class ProjectGroupTest(TestCase):
    def test_save_project_group(self):
        project_group = ProjectGroup()
        project_group.name = 'Pronto World'
        project_group.slug = 'pronto-world'
        project_group.description = 'Pronto World Group'
        project_group.save()

        project_group = ProjectGroup.objects.last()

        self.assertEqual(project_group.name, 'Pronto World')
        self.assertEqual(project_group.slug, 'pronto-world')
        self.assertEqual(project_group.description, 'Pronto World Group')

    def test_project_group_should_have_friendly_name(self):
        project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )
        self.assertEqual(project_group.__str__(), 'Pronto World')
