# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0003_auto_20151104_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='unit',
            field=models.ForeignKey(to='cdpapp.Unit'),
        ),
    ]
