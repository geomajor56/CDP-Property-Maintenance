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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('property_name', models.CharField(max_length=30, help_text='Enter full name, must be unique')),
                ('address', models.CharField(max_length=200, blank=True)),
                ('town', models.CharField(max_length=30, blank=True)),
                ('state', models.CharField(default='MA', max_length=2)),
                ('zip', models.CharField(max_length=10, null=True, blank=True)),
                ('building_comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(default='tenant@gmail.com', max_length=254, blank=True)),
                ('primary_phone', models.CharField(default='1234567893', max_length=10, null=True, blank=True)),
                ('property_name', models.ForeignKey(related_name='tenant_property', to='cdpapp.Building')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('unit', models.CharField(max_length=30)),
                ('bedrooms', models.IntegerField(default=1)),
                ('bathrooms', models.DecimalField(default=1.0, decimal_places=1, max_digits=2)),
                ('unit_comments', models.TextField(blank=True)),
                ('property_name', models.ForeignKey(related_name='units', to='cdpapp.Building')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('ordernum', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.CharField(default='Not so urgent', max_length=20, choices=[('Urgent', 'Urgent'), ('Not so urgent', 'Not so Urgent'), ('Whenever', 'Whenever')])),
                ('request_by', models.CharField(default='Resident', max_length=20, choices=[('Staff', 'Staff'), ('Resident', 'Resident'), ('Inspection', 'Inspection'), ('Other', 'Other')])),
                ('call_date', models.DateField(blank=True)),
                ('problem_desc', models.TextField(blank=True)),
                ('complete_by', models.DateField(null=True, blank=True)),
                ('completed_by', models.TextField(default='Staff', max_length=25, choices=[('Staff', 'Staff'), ('Contractor', 'Contractor'), ('Other', 'Other')])),
                ('completed', models.BooleanField(default=False)),
                ('complete_date', models.DateField(null=True, blank=True)),
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
