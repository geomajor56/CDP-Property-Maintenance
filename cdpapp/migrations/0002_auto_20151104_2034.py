# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='property_name',
            new_name='building',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='property_name',
            new_name='building',
        ),
        migrations.RenameField(
            model_name='workorder',
            old_name='property_name',
            new_name='building',
        ),
    ]
