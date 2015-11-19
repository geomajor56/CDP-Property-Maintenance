from django.conf.urls import url
from . import views
# from cdpapp.views import BuildingList, BuildingDetail, BuildingUnitDetail, CreateWorkOrder, EditWorkOrder,\
#     DeleteWorkOrder, ListAllWorkOrders #list_all_workorders

from cdpapp.views import BuildingList, BuildingDetail, BuildingUnitDetail, ListAllWorkOrders, CreateWorkOrder, EditWorkOrder, DeleteWorkOrder

urlpatterns = [
    url(r'^$', BuildingList.as_view(), name='index'),
    url(r'^building/(?P<pk>\d+)/$', BuildingDetail.as_view(), name='building_detail'),
    url(r'^unit/(?P<pk>\d+)/$', BuildingUnitDetail.as_view(), name='building_unit_detail'),

    url(r'^workorder/create/$', CreateWorkOrder.as_view(), name='workorder_add'),
    url(r'^workorder/edit/(?P<pk>\d+)/$', EditWorkOrder.as_view(), name='workorder_update'),
    url(r'^workorder/delete/(?P<pk>\d+)/delete/$', DeleteWorkOrder.as_view(), name='workorder_delete'),
    # url(r'^workorder/all/$', list_all_workorders, name='list_all_workorders'),
     url(r'^workorder/all/$', ListAllWorkOrders.as_view(), name='list_all_workorders'),
]
