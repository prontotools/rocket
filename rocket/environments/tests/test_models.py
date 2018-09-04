from django.test import TestCase

from ..models import Environment
from projects.models import (
    Project,
    ProjectGroup,
)


class EnvironmentTest(TestCase):
    def test_save_environment(self):
        project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )
        project = Project.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Description',
            project_group=project_group
        )

        env = Environment()
        env.name = 'Production'
        env.project = project
        env.save()

        env = Environment.objects.last()

        self.assertEqual(env.name, 'Production')
        self.assertEqual(env.project.id, project.id)

    def test_environment_should_have_friendly_name(self):
        project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )
        project = Project.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Description',
            project_group=project_group
        )
        env = Environment.objects.create(
            name='Production',
            project=project
        )

        self.assertEqual(env.__str__(), 'Pronto World: Production')
