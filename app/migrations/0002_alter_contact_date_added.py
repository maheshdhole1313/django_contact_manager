# Generated by Django 3.2.9 on 2021-11-24 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
