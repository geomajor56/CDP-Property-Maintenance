import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from cdpapp.models import WorkOrder


class WorkOrderTable(tables.Table):
    class Meta:
        model = WorkOrder
        fields = ("call_date", "ordernum", "building", "unit", "request_by", 'problem_desc', 'completed')
        attrs = {"class": "paleblue"}

    # property_name = tables.Column
    # unit = tables.Column
    # request_by = tables.Column
    # problem_desc = tables.Column
    # ordernum = tables.LinkColumn('workorder_detail', args=[A('pk')])
    # call_date = tables.Column
    # edit_link = tables.LinkColumn('workorder_update', args=[A('pk')],
    #                               verbose_name='Edit', accessor='pk', attrs={'class': 'edit_link'})
    # delete_link = tables.LinkColumn('workorder_delete', args=[A('pk')],
                                    # verbose_name='Delete Work Order', accessor='pk', attrs={'class': 'delete_link'})
    #
    # class Meta:
    #     model = WorkOrder
    #     fields = ("call_date", "ordernum", "building", "unit", "request_by", 'problem_desc')