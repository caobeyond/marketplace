# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160618_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]