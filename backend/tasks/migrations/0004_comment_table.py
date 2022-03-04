# Generated by Django 3.2.8 on 2021-10-16 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_personal_data_table'),
        ('tasks', '0003_task_table_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee')),
                ('task', models.ManyToManyField(to='tasks.Task')),
            ],
        ),
    ]