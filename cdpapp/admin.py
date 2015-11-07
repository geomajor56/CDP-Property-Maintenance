from django.contrib import admin
from .models import Building, Unit, Tenant, WorkOrder


class WorkorderAdmin(admin.ModelAdmin):
    list_display = (
        'building', 'unit', 'request_by', 'call_date', 'problem_desc', 'complete_by', 'complete_date', 'priority')


class UnitAdmin(admin.ModelAdmin):
    list_display = ('building', 'unit', 'bedrooms', 'bathrooms', 'unit_comments')


class TenantAdmin(admin.ModelAdmin):
    list_display = ('building', 'unit', 'first_name', 'last_name', 'email')

admin.site.register(Building)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(WorkOrder, WorkorderAdmin)
