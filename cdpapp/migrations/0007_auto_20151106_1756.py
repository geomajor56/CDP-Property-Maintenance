# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0006_auto_20151106_0842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenant',
            options={},
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='primary_phone',
        ),
    ]
