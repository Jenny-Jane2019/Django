# Generated by Django 3.1.1 on 2021-03-26 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0020_auto_20210323_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='environment',
            field=models.CharField(choices=[('living room', 'living room'), ('dormitory', 'dormitory'), ('bedroom', 'bedroom'), ('study', 'study'), ('Other', 'Other')], default='living room', max_length=200),
        ),
    ]
