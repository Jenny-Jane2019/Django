# Generated by Django 3.1.1 on 2020-11-27 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP', '0012_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='age',
            new_name='speaker_age',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='file',
            new_name='speaker_file',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='speaker_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='sex',
            new_name='speaker_sex',
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
