# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160715_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorproductproperty',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_product_property_product_vendor', to='store.Vendor'),
        ),
        migrations.AlterField(
            model_name='vendorproductproperty',
            name='value_text',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
