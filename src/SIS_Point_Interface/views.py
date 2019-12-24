from datetime import datetime

from django.core import serializers
from django.shortcuts import render
import json
import time
import re
# Create your views here.

from django.http import JsonResponse
from django.db import connection

# 这两个可以放在同一个请求里
from SIS_Point_Interface import models


def get_sis_realtime_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_sis_realtime` where id = (SELECT MAX(id) FROM smcs_sis_realtime);")
    newest_record = cursor.fetchone()
    return JsonResponse(newest_record, safe=False)


def get_sis_flag_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_sis_flag` where id = (SELECT MAX(id) FROM smcs_sis_flag);")
    newest_record = cursor.fetchone()
    return JsonResponse(newest_record, safe=False)


def get_sis_column_list(request):
    cursor = connection.cursor()
    cursor.execute("select COLUMN_NAME from information_schema.COLUMNS "
                   "where table_name = 'smcs_sis_realtime' and table_schema = 'smcs';")
    newest_record = cursor.fetchall()
    response_content = newest_record[2] + newest_record[3] + newest_record[4]
    return JsonResponse(response_content, safe=False)
    # print(newest_record[2:5])


def post_data_analysis_traffic_search(request):
    post_content = json.loads(request.body, encoding='utf-8')
    start_date = datetime.strptime(post_content['startTime'], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(post_content['endTime'], '%Y-%m-%d %H:%M:%S')
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    column_name = re.findall(p1, post_content['node'][0]['label'])[0]
    data_series = models.SISRealtime.objects.filter(add_time__range=(start_date, end_date)).\
        values_list('add_time', column_name)
    # 这地方是建立一个dict，用于json化返回
    data_series_dict = {}
    for e in data_series:
        data_series_dict[e[0].strftime('%Y-%m-%d %H:%M:%S')] = round(e[1], 3)
    # print(data_series_dict)
    return JsonResponse(data_series_dict, safe=False)
