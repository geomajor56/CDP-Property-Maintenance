from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from cdpapp.models import Building, Unit, Tenant, WorkOrder
from django.forms import ModelForm, TextInput, Select


class WorkOrderForm(forms.ModelForm):
    next = forms.CharField(required=False)

    class Meta:
        model = WorkOrder
        fields = ['building', 'unit', 'ordernum', 'call_date', 'request_by', 'problem_desc']



        # fields = tuple()  # class WorkOrderForm(forms.Form):
#     building = forms.ModelChoiceField(queryset=Building.objects.all())
#     unit = forms.ModelChoiceField(queryset=Unit.objects.all())
#     call_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
#     request_by = forms.CharField()
#     problem_desc = forms.CharField(widget=forms.Textarea)
#     complete_by = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
#     completed = forms.BooleanField()
#     complete_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
#     maint_comments = forms.CharField(widget=forms.Textarea)


#
#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.form_class = 'form-horizontal'
#     helper.label_class = 'col-sm-2'
#     helper.field_class = 'col-sm-4'
#     helper.layout = Layout(
#         Field('building', css_class='input-sm'),
#         Field('unit', css_class='input-sm'),
#         Field('call_date', css_class='input-sm'),
#         Field('request_by', css_class='input-sm'),
#         Field('problem_desc', rows=5),
#         Field('complete_by', css_class='input-sm'),
#         Field('completed', css_class='input-sm'),
#         Field('complete_date', css_class='input-sm'),
#         Field('maint_comments', rows=5),
#         FormActions(Submit('submit', 'submit', css_class='btn-primary'))
#     )
