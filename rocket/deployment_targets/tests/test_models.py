from django.test import TestCase

from ..models import DeploymentTarget
from environments.models import Environment
from projects.models import (
    Project,
    ProjectGroup,
)


class DeploymentTargetTest(TestCase):
    def test_save_deployment_target(self):
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
        environment = Environment.objects.create(
            name='Production',
            project=project
        )

        deployment_target = DeploymentTarget()
        deployment_target.name = 'Pronto World Test Server'
        deployment_target.ip = '52.130.21.244'
        deployment_target.environment = environment
        deployment_target.save()

        deployment_target = DeploymentTarget.objects.last()

        self.assertEqual(deployment_target.name, 'Pronto World Test Server')
        self.assertEqual(deployment_target.ip, '52.130.21.244')
        self.assertEqual(deployment_target.environment.id, environment.id)
