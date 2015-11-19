from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from cdpapp.models import Building, Unit, Tenant, WorkOrder
from django.forms import ModelForm, TextInput, Select
import floppyforms.__future__ as forms


class WorkOrderForm(forms.ModelForm):
    # next = forms.CharField(required=False)

    class Meta:
        model = WorkOrder
        fields = ['building', 'unit', 'request_by', 'call_date', 'problem_desc', 'complete_by', 'complete_date', 'completed', 'maint_comments']
