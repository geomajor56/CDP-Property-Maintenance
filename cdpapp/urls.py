from django.conf.urls import url
from . import views
from cdpapp.views import BuildingList, BuildingDetail, BuildingUnitDetail

urlpatterns = [
    url(r'^$', BuildingList.as_view(), name='index'),
    url(r'^building/(?P<pk>\d+)/$', BuildingDetail.as_view(), name='building_detail'),
    url(r'^unit/(?P<pk>\d+)/$', BuildingUnitDetail.as_view(), name='building_unit_detail'),
]
