# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20160727_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
