# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0009_auto_20151110_0726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'Property', 'ordering': ['property_name'], 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Unit', 'ordering': ['unit'], 'verbose_name_plural': 'Units'},
        ),
    ]
