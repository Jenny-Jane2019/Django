# Generated by Django 3.1.1 on 2020-11-23 14:29

import APP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_auto_20201123_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='file',
            field=models.FileField(null=True),
        ),
    ]
