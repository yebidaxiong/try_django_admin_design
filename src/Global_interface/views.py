from datetime import datetime

from django.core import serializers
from django.shortcuts import render
import json
import time
import re
# Create your views here.

from django.http import JsonResponse
from django.db import connection

from DCS_Point_Interface.models import DCSPoint
from GAS_Point_Interface.models import GASPoint
from SIS_Point_Interface.models import SISPoint


def search_online_point_dp_drawer(request):
    post_content = json.loads(request.body, encoding='utf-8')
    # print(post_content)
    table_type = post_content.get('Type')
    table = None

    if table_type == 'SIS':
        table = SISPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    elif table_type == 'GDS':
        table = GASPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    elif table_type == 'DCS':
        table = DCSPoint.objects.filter(point_add_to_service=1) \
            .values_list('id', 'point_name', 'point_code', 'point_category', 'point_connection_status', 'is_tab')
    table_list = list(table)
    # for e in table:
    #     table_series_dict['point_code'] = round(e[1], 3)
    # print(table_list)
    # print(table_type)
    return JsonResponse(table_list, safe=False)
