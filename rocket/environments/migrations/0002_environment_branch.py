# Generated by Django 2.1.1 on 2018-09-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='branch',
            field=models.CharField(default='develop', max_length=100),
        ),
    ]
