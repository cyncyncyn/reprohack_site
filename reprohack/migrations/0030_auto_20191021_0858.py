# Generated by Django 2.2.6 on 2019-10-21 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0029_auto_20191020_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 29, 766335)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 29, 766287)),
        ),
    ]