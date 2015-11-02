# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('property_name', models.CharField(help_text='Enter full name, must be unique', max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('town', models.CharField(blank=True, max_length=30)),
                ('zip', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, default='tenant@gmail.com', max_length=254)),
                ('primary_phone', models.CharField(blank=True, null=True, default='1234567893', max_length=10)),
                ('property_name', models.ForeignKey(related_name='tenant_property', to='cdpapp.Building')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('unit', models.CharField(max_length=30)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.DecimalField(max_digits=2, decimal_places=1, default=1.0)),
                ('property_name', models.ForeignKey(related_name='units', to='cdpapp.Building')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('ordernum', models.AutoField(serialize=False, primary_key=True)),
                ('priority', models.CharField(default='Not so urgent', choices=[('Urgent', 'Urgent'), ('Not so urgent', 'Not so Urgent'), ('Whenever', 'Whenever')], max_length=20)),
                ('request_by', models.CharField(default='Resident', choices=[('Staff', 'Staff'), ('Resident', 'Resident'), ('Inspection', 'Inspection'), ('Other', 'Other')], max_length=20)),
                ('call_date', models.DateField(blank=True)),
                ('problem_desc', models.TextField()),
                ('complete_by', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('complete_date', models.DateField(blank=True, null=True)),
                ('maint_comments', models.TextField(blank=True)),
                ('property_name', models.ForeignKey(related_name='workorder_property', to='cdpapp.Building')),
                ('unit', models.ForeignKey(related_name='workorder_unit', to='cdpapp.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='unit',
            field=models.ForeignKey(related_name='tenant_unit', to='cdpapp.Unit'),
        ),
    ]
