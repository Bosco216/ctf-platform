# Generated by Django 3.1.8 on 2021-04-16 12:42

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210416_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='solved_problems',
            field=django_mysql.models.ListTextField(models.IntegerField(), blank=True, null=True, size=100),
        ),
    ]
