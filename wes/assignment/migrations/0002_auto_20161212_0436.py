# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalDetails',
            new_name='Assignment',
        ),
    ]
