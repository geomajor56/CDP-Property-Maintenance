# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0007_auto_20151106_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'Property'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Unit'},
        ),
        migrations.AlterModelOptions(
            name='workorder',
            options={'verbose_name_plural': 'Work Orders', 'verbose_name': 'Work Order'},
        ),
    ]
