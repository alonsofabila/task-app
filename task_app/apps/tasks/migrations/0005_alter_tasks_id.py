# Generated by Django 5.0.4 on 2024-05-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_tasks_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.CharField(default='task-3f1b7bdb51', editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]
