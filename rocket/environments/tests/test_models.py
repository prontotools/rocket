from django.test import TestCase

from ..models import Environment
from projects.models import (
    Project,
    ProjectGroup,
)


class EnvironmentTest(TestCase):
    def setUp(self):
        self.project_group = ProjectGroup.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Group'
        )
        self.project = Project.objects.create(
            name='Pronto World',
            slug='pronto-world',
            description='Pronto World Description',
            project_group=self.project_group
        )

    def test_save_environment(self):
        env = Environment()
        env.name = 'Production'
        env.project = self.project
        env.save()

        env = Environment.objects.last()

        self.assertEqual(env.name, 'Production')
        self.assertEqual(env.project.id, self.project.id)

    def test_environment_should_have_friendly_name(self):
        env = Environment.objects.create(
            name='Production',
            project=self.project
        )
        self.assertEqual(env.__str__(), 'Pronto World: Production')
