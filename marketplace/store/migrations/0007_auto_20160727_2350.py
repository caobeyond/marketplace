# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160715_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='type_rule',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]