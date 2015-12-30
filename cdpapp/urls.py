from django.conf.urls import url
from cdpapp.views import BuildingList, BuildingDetail, BuildingUnitDetail, \
    ListAllWorkOrders, CreateWorkOrder, EditWorkOrder, DeleteWorkOrder, some_view


urlpatterns = [
    url(r'^$', BuildingList.as_view(), name='index'),
    url(r'^building/(?P<pk>\d+)/$', BuildingDetail.as_view(), name='building_detail'),
    url(r'^unit/(?P<pk>\d+)/$', BuildingUnitDetail.as_view(), name='building_unit_detail'),

    url(r'^workorder/create/$', CreateWorkOrder.as_view(), name='workorder_add'),
    url(r'^workorder/edit/(?P<pk>\d+)/$', EditWorkOrder.as_view(), name='workorder_update'),
    url(r'^workorder/delete/(?P<pk>\d+)/delete/$', DeleteWorkOrder.as_view(), name='workorder_delete'),
    url(r'^workorder/all/$', ListAllWorkOrders.as_view(), name='list_all_workorders'),

    url(r'^easy$', some_view),

]
