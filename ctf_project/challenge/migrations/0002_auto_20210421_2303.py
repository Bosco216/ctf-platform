# Generated by Django 3.1.8 on 2021-04-21 15:03

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='solved_problems',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), blank=True, default='99999999999999999999999999', null=True, size=100),
        ),
    ]
