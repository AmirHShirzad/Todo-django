# Generated by Django 3.2.15 on 2022-08-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_todo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]
