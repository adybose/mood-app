# Generated by Django 2.0.2 on 2019-06-21 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 21, 19, 45, 0, 858098)),
        ),
    ]
