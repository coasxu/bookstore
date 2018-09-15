# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-14 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import mainsite.system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20180914_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(storage=mainsite.system.storage.ImageStorage(), upload_to='img/%Y/%m/%d'),
        ),
    ]
