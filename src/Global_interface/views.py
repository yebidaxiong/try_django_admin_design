from datetime import datetime

import json
# Create your views here.
from django.db import connection
from django.http import JsonResponse

from DCS_Point_Interface.models import DCSPoint
from GAS_Point_Interface.models import GASPoint
from SIS_Point_Interface.models import SISPoint

# global table name during drawer opening
from Schedule_Job.views import db_backup

current_table_name = ''


def search_online_point_dp_drawer(request):
    post_content = json.loads(request.body, encoding='utf-8')
    # print(post_content)
    table_type = post_content.get('Type')
    table = None

    if table_type == 'SIS':
        edit_current_table_name('SIS')
        table = SISPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    elif table_type == 'GDS':
        edit_current_table_name('GDS')
        table = GASPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    elif table_type == 'DCS':
        edit_current_table_name('DCS')
        table = DCSPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    table_list = list(table)
    return JsonResponse(table_list, safe=False)


# from backend get table name, waive network cost
# TODO: whats wrong with global variables
def edit_current_table_name(table_name):
    global current_table_name
    current_table_name = table_name
    # print(current_table_name)


# for updating is_table column to 1 when point card is selected
# TODO: only add, no delete, 0 to 1 is ok, 1 to 0 is not, frontend: select but not submit(good),
#  logically right currently
def tabed_point_dp(request):
    post_content = json.loads(request.body, encoding='utf-8')
    # print(post_content) O(n) acceptable !
    post_content_list = []
    for element in range(len(post_content)):
        post_content_list.append(post_content[element]['PointCode'])
    # print(post_content_list)
    # print(current_table_name)
    if current_table_name == 'SIS':
        SISPoint.objects.filter(point_code__in=post_content_list).update(is_tab=True)
        SISPoint.objects.exclude(point_code__in=post_content_list).update(is_tab=False)
    elif current_table_name == 'GDS':
        GASPoint.objects.filter(point_code__in=post_content_list).update(is_tab=True)
        GASPoint.objects.exclude(point_code__in=post_content_list).update(is_tab=False)
    elif current_table_name == 'DCS':
        DCSPoint.objects.filter(point_code__in=post_content_list).update(is_tab=True)
        DCSPoint.objects.exclude(point_code__in=post_content_list).update(is_tab=False)
    else:
        print("no match")
    edit_current_table_name('')

    # 在这里加入返回所有is_tab等于1的三个表数据，拼接，发给前端，有一个逻辑要注意，保证在上次添加之后执行
    # 这个列表保存全部is_tab为1的点，返回point_name, point_code, point_category

    return JsonResponse(get_global_selected_point(), safe=False)


def get_global_selected_point():
    global_selected_point = []
    for ele in range(len(list(SISPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                               'point_category', 'point_unit')))):
        global_selected_point.append(
            list(SISPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                  'point_category', 'point_unit'))[ele])

    for ele in range(len(list(GASPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                               'point_category', 'point_unit')))):
        global_selected_point.append(
            list(GASPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                  'point_category', 'point_unit'))[ele])

    for ele in range(len(list(DCSPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                               'point_category', 'point_unit')))):
        global_selected_point.append(
            list(DCSPoint.objects.filter(is_tab=True).values_list('id', 'point_name', 'point_code',
                                                                  'point_category', 'point_unit'))[ele])
    return global_selected_point
