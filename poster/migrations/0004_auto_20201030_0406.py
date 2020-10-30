# Generated by Django 3.1.2 on 2020-10-30 04:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0003_auto_20201020_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.DateTimeField(default=datetime.datetime(2020, 10, 30, 4, 6, 11, 458585, tzinfo=utc), verbose_name='Active')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, verbose_name='e-mail')),
                ('phone_number', models.IntegerField(verbose_name='Phone Number')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='professor',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 4, 6, 11, 458585, tzinfo=utc), verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='modified',
            field=models.DateField(auto_now=True, verbose_name='Modified'),
        ),
    ]
