# Generated by Django 3.1.1 on 2020-11-27 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0010_auto_20201127_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
