# Generated by Django 3.2.8 on 2021-11-23 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_project_no_time_fix'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]