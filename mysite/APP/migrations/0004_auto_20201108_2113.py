# Generated by Django 3.1.1 on 2020-11-08 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP', '0003_auto_20201108_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='speech',
            name='age',
            field=models.CharField(choices=[('<20', '<20'), ('20-40', '20-40'), ('40-60', '40-60'), ('>60', '>60')], default='20-40', max_length=200),
        ),
        migrations.AlterField(
            model_name='speech',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=200),
        ),
    ]