# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0004_auto_20151105_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building', related_name='tenant_building'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='unit',
            field=models.ForeignKey(to='cdpapp.Unit', related_name='tenant_unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building', related_name='unit_building'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building', related_name='workorder_building'),
        ),
    ]
