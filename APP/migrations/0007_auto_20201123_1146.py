# Generated by Django 3.1.1 on 2020-11-23 03:46

import APP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_auto_20201120_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='audio_file',
            field=models.FileField(blank=True, null=True),
        ),
    ]