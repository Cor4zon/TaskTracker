# Generated by Django 3.2.8 on 2021-10-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_tasks_no_default_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True),
        ),
    ]
