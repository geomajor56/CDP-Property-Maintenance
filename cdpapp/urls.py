from django.conf.urls import url
from . import views
from cdpapp.views import BuildingList, BuildingDetail, BuildingUnitDetail, CreateWorkOrder, EditWorkOrder,\
    DeleteWorkOrder, list_all_workorders


urlpatterns = [
    url(r'^$', BuildingList.as_view(), name='index'),
    url(r'^building/(?P<pk>\d+)/$', BuildingDetail.as_view(), name='building_detail'),
    url(r'^unit/(?P<pk>\d+)/$', BuildingUnitDetail.as_view(), name='building_unit_detail'),

    url(r'^workorder/add/$', CreateWorkOrder.as_view(), name='workorder_add'),
    url(r'^workorder/(?P<pk>\d+)/$', EditWorkOrder.as_view(), name='workorder_update'),
    url(r'^workorder/(?P<pk>\d+)/delete/$', DeleteWorkOrder.as_view(), name='workorder_delete'),
    url(r'^workorder/all/$', list_all_workorders, name='list_all_workorders'),
]
