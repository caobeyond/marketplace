# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-13 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20170103_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='status',
            field=models.IntegerField(choices=[(0, b'Open'), (1, b'Pending'), (2, b'Processing'), (3, b'Cancelled'), (4, b'Complete'), (5, b'Shipping'), (6, b'Closed'), (7, b'Unpaid'), (8, b'Recommended'), (9, b'Declined'), (99, b'Error')]),
        ),
    ]
