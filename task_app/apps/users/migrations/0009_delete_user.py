# Generated by Django 5.0.4 on 2024-05-06 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_tasks_created_by_alter_tasks_id'),
        ('users', '0008_alter_user_managers_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
