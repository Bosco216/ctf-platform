# Generated by Django 3.1.8 on 2021-04-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20210412_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='competition',
        ),
        migrations.AlterField(
            model_name='competition',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='competition',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
