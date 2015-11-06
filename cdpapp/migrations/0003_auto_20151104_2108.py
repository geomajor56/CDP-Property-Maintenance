# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0002_auto_20151104_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building'),
        ),
    ]
