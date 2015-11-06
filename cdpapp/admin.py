from django.contrib import admin
from .models import Building, Unit, Tenant, WorkOrder


class WorkorderAdmin(admin.ModelAdmin):
    list_display = (
        'building', 'unit', 'request_by', 'call_date', 'problem_desc', 'complete_by', 'complete_date', 'priority')


admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(WorkOrder, WorkorderAdmin)
