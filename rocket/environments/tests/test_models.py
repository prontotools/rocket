from django.test import TestCase

from ..models import Environment


class EnvironmentTest(TestCase):
    def test_save_environment(self):
        env = Environment()
        env.name = 'Production'
        env.save()

        env = Environment.objects.last()

        self.assertEqual(env.name, 'Production')
