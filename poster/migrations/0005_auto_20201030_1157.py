# Generated by Django 3.1.2 on 2020-10-30 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0004_auto_20201030_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 11, 57, 50, 333576, tzinfo=utc), verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 11, 57, 50, 333576, tzinfo=utc), verbose_name='Active'),
        ),
    ]
