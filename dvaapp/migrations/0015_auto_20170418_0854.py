# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0014_clustercodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clustercodes',
            name='coarse_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='clustercodes',
            name='fine_text',
            field=models.TextField(default=''),
        ),
    ]
