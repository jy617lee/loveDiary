# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-06 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='update_date',
            field=models.DateField(),
        ),
    ]
