# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170131_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='parametr',
            field=models.CharField(max_length=15),
        ),
    ]
