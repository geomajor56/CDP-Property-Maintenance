from django import forms

from cdpapp.models import WorkOrder


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('building', 'unit', 'call_date', 'request_by', 'problem_desc', 'complete_by', 'completed', 'complete_date')

