from django.db import models
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


class Unit(models.Model):
    building = models.ForeignKey(Building)
    unit = models.CharField(max_length=30)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    unit_comments = models.TextField(blank=True)

    def __str__(self):
        return '%s %s' % (self.building, self.unit)


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

    building = models.ForeignKey(Building)
    unit = models.ForeignKey(Unit)
    ordernum = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=20, choices=PRIORITY, default='Not so urgent')
    request_by = models.CharField(max_length=20, choices=REQUEST_BY, default='Resident')
    call_date = models.DateField(blank=True)
    problem_desc = models.TextField(blank=True)
    complete_by = models.DateField(null=True, blank=True)
    completed_by = models.TextField(max_length=25, choices=COMPLETED_BY, default='Staff')
    completed = models.BooleanField(default=False, blank=True)
    complete_date = models.DateField(null=True, blank=True, auto_now_add=False)
    maint_comments = models.TextField(blank=True)

    def __str__(self):
        return '%s %s' % (self.building, self.unit)
