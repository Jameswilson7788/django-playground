# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-07 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]
