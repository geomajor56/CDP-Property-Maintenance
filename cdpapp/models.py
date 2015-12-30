from django.db import models
from smart_selects.db_fields import ChainedForeignKey
import datetime


class Building(models.Model):
    property_name = models.CharField(max_length=30, help_text='Enter full name, must be unique')
    address = models.CharField(max_length=200, blank=True)
    town = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, default='MA')
    zip = models.CharField(max_length=10, null=True, blank=True)
    building_comments = models.TextField(blank=True)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        ordering = ['property_name']


class Unit(models.Model):
    building = models.ForeignKey(Building)
    unit = models.CharField(max_length=30)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    unit_comments = models.TextField(blank=True)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ['unit']


class Tenant(models.Model):
    building = models.ForeignKey(Building)
    unit = models.ForeignKey(Unit)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, default="tenant@gmail.com")


def __str__(self):
    return u'%s %s %s' % (self.unit, self.first_name, self.last_name)


class Meta:
    ordering = ['last_name']
    verbose_name = 'Tenant'


class WorkOrder(models.Model):
    PRIORITY = (
        ('Urgent', 'Urgent'),
        ('Not so urgent', 'Not so Urgent'),
        ('Whenever', 'Whenever'),
    )

    REQUEST_BY = (
        ('Staff', 'Staff'),
        ('Resident', 'Resident'),
        ('Inspection', 'Inspection'),
        ('Other', 'Other'),
    )

    COMPLETED_BY = (
        ('Staff', 'Staff'),
        ('Contractor', 'Contractor'),
        ('Other', 'Other'),
    )

    building = models.ForeignKey(Building, verbose_name='Property')
    unit = ChainedForeignKey(
            Unit,
            chained_field="building",
            chained_model_field="building",
            show_all=False,
            auto_choose=True
    )
    ordernum = models.AutoField(primary_key=True, verbose_name='Order #')
    priority = models.CharField(verbose_name='Priority', max_length=20, choices=PRIORITY, default='Not so urgent')
    request_by = models.CharField(verbose_name='Requested By', max_length=20, choices=REQUEST_BY, default='Resident')
    call_date = models.DateField(default=datetime.date.today, verbose_name='Date Reported', blank=True)
    problem_desc = models.TextField(verbose_name='Description', blank=True)
    complete_by = models.DateField(verbose_name='Complete By', null=True, blank=True)
    completed_by = models.TextField(verbose_name='Completed By', max_length=25, choices=COMPLETED_BY, default='Staff')
    completed = models.BooleanField(verbose_name='Completed?', default=False, blank=True)
    complete_date = models.DateField(verbose_name='Complete Date', null=True, blank=True, auto_now_add=False)
    maint_comments = models.TextField(verbose_name='Comments', blank=True)

    def __str__(self):
        return '%s %s' % (self.building, self.unit)

    @property
    def checkbox_character(self):
        return '☑' if self.complete else '☐'

    class Meta:
        ordering = ['building', 'unit', 'call_date']
        verbose_name = 'Work Order'
        verbose_name_plural = 'Work Orders'
