# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdpapp', '0008_auto_20151110_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='building',
            field=models.ForeignKey(to='cdpapp.Building', verbose_name='Property'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='call_date',
            field=models.DateField(blank=True, verbose_name='Call Date'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='complete_by',
            field=models.DateField(null=True, blank=True, verbose_name='Complete By'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='complete_date',
            field=models.DateField(null=True, blank=True, verbose_name='Complete Date'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed?'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='completed_by',
            field=models.TextField(default='Staff', max_length=25, choices=[('Staff', 'Staff'), ('Contractor', 'Contractor'), ('Other', 'Other')], verbose_name='Completed By'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='maint_comments',
            field=models.TextField(blank=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='ordernum',
            field=models.AutoField(serialize=False, verbose_name='Order #', primary_key=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='priority',
            field=models.CharField(default='Not so urgent', max_length=20, choices=[('Urgent', 'Urgent'), ('Not so urgent', 'Not so Urgent'), ('Whenever', 'Whenever')], verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='problem_desc',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='request_by',
            field=models.CharField(default='Resident', max_length=20, choices=[('Staff', 'Staff'), ('Resident', 'Resident'), ('Inspection', 'Inspection'), ('Other', 'Other')], verbose_name='Requested By'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='unit',
            field=models.ForeignKey(to='cdpapp.Unit', verbose_name='Unit'),
        ),
    ]
