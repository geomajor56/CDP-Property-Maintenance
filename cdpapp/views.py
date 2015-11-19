from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect
from django.http import JsonResponse
from django_tables2 import RequestConfig
from cdpapp.tables import WorkOrderTable
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from cdpapp.models import Building, Unit, WorkOrder
from cdpapp.forms import WorkOrderForm

from vanilla import CreateView, DeleteView, ListView, UpdateView


class BuildingList(ListView):
    model = Building
    template_name = 'cdpapp/index.html'
    context_object_name = 'buildings'


class BuildingDetail(DetailView):
    model = Building
    template_name = 'cdpapp/building_detail.html'
    context_object_name = 'buildings_detail'


class BuildingUnitDetail(DetailView):
    model = Unit
    template_name = 'cdpapp/building_units_detail.html'
    context_object_name = 'units'


class ListAllWorkOrders(ListView):
    template_name = 'cdpapp/workorder_all_list.html'
    model = WorkOrder


class CreateWorkOrder(CreateView):
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy('list_all_workorders')


class EditWorkOrder(UpdateView):
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy('list_all_workorders')


class DeleteWorkOrder(DeleteView):
    model = WorkOrder
    success_url = reverse_lazy('list_all_workorders')





# class CreateWorkOrder(CreateView):
#     template_name = 'cdpapp/workorder_form.html'
#     model = WorkOrder
#     form_class = WorkOrderForm
#
#     def get_form_kwargs(self, **kwargs):
#         kwargs = super(CreateWorkOrder, self).get_form_kwargs()
#         redirect = self.request.GET.get('next')
#         if redirect:
#             if 'initial' in kwargs.keys():
#                 kwargs['initial'].update({'next': redirect})
#             else:
#                 kwargs['initial'] = {'next': redirect}
#         return kwargs
#
#     def form_valid(self, form):
#         redirect = form.cleaned_data.get('next')
#         if redirect:
#             self.success_url = redirect
#         return super(CreateWorkOrder, self).form_valid(form)


# class EditWorkOrder(UpdateView):
#     template_name = 'cdpapp/workorder_form.html'
#     model = WorkOrder
#     form_class = WorkOrderForm


# def get_form_kwargs(self, **kwargs):
#     kwargs = super(EditWorkOrder, self).get_form_kwargs()
#     redirect = self.request.GET.get('next')
#     if redirect:
#         if 'initial' in kwargs.keys():
#             kwargs['initial'].update({'next': redirect})
#         else:
#             kwargs['initial'] = {'next': redirect}
#     return kwargs


# def form_valid(self, form):
#     redirect = form.cleaned_data.get('next')
#     if redirect:
#         self.success_url = redirect
#     return super(EditWorkOrder, self).form_valid(form)
#
#     # template_name = 'cdpapp/workorder_form.html'
#     # model = WorkOrder
#     # fields = ['building', 'unit', 'request_by', 'call_date', 'problem_desc',
#     #           'complete_by', 'complete_date', 'completed', 'maint_comments']
#     # success_url = reverse_lazy('building_unit_detail')


# class DeleteWorkOrder(DeleteView):
#     template_name = 'cdpapp/workorder_form.html'
#     model = WorkOrder
#     success_url = reverse_lazy('list_workorders')


# class ListWorkOrder(ListView):
#     template_name = 'cdpapp/workorder_all_list.html'
#     model = WorkOrder
#     context_object_name = 'workorder_list'





# def list_all_workorders(request):
#     table = WorkOrderTable(WorkOrder.objects.all())
#     RequestConfig(request, paginate={"per_page": 10}).configure(table)
#     # return render(request, "cdpapp/workorder_all_list.html", {"wo": WorkOrder.objects.all()})
#     # RequestConfig(request).configure(table)
#     return render(request, 'cdpapp/workorder_all_list.html', {'table': table})
