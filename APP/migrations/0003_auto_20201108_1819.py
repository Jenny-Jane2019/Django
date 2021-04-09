# Generated by Django 3.1.1 on 2020-11-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20201108_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='age',
            field=models.CharField(choices=[('<20', '20-30'), ('30-40', '40-50'), ('50-60', '>60')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='speech',
            name='sex',
            field=models.CharField(choices=[('male', 'female')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='speech',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]