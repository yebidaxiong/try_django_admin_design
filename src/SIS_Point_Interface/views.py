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
    cursor.execute("SELECT * FROM \"SMCS_SIS_REALTIME\" where id = (SELECT MAX(id) FROM \"SMCS_SIS_REALTIME\");")
    newest_record = cursor.fetchone()
    return JsonResponse(newest_record, safe=False)


def get_sis_flag_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM \"SMCS_SIS_Flag\" where id = (SELECT MAX(id) FROM \"SMCS_SIS_Flag\");")
    newest_record = cursor.fetchone()
    return JsonResponse(newest_record, safe=False)


def get_sis_column_list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT column_name FROM information_schema.columns "
                   "WHERE table_schema = 'public' and table_name='SMCS_SIS_REALTIME'")
    newest_record = cursor.fetchall()
    response_content = newest_record[2] + newest_record[3] + newest_record[4]
    # print(response_content)
    return JsonResponse(response_content, safe=False)
    # print(newest_record[2:5])


def post_data_analysis_traffic_search(request):
    # 获得post请求体数据
    post_content = json.loads(request.body, encoding='utf-8')
    # 拿到开始与结束日期
    start_date = datetime.strptime(post_content['startTime'], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(post_content['endTime'], '%Y-%m-%d %H:%M:%S')
    # TODO：拆解字符串拿到点名，这个地方应该优化，现在是拿到括号内字符串，这个逻辑显然不行，需要迭代
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    column_name = re.findall(p1, post_content['node'][0]['label'])[0]
    # ORM获取数据
    data_series = models.SISRealtime.objects.filter(add_time__range=(start_date, end_date)).\
        values_list('add_time', column_name)
    # 这地方是建立一个dict，用于json化返回，因为ORM获取数据为QuerySet，不能Json化，我认为这个地方应该有更好的方式
    data_series_dict = {}
    for e in data_series:
        data_series_dict[e[0].strftime('%Y-%m-%d %H:%M:%S')] = round(e[1], 3)
    return JsonResponse(data_series_dict, safe=False)


def post_data_analysis_alarm_search(request):
    # 获得post请求体数据
    post_content = json.loads(request.body, encoding='utf-8')
    # 拿到开始与结束日期
    start_date = datetime.strptime(post_content['startTime'], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(post_content['endTime'], '%Y-%m-%d %H:%M:%S')
    # TODO：拆解字符串拿到点名，这个地方应该优化，现在是拿到括号内字符串，这个逻辑显然不行，需要迭代
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    column_name = re.findall(p1, post_content['node'][0]['label'])[0] + "_flag"
    # ORM获取数据
    data_series = models.SISFlag.objects.filter(add_time__range=(start_date, end_date)). \
        values_list('add_time', column_name)
    # 这地方是建立一个dict，用于json化返回，因为ORM获取数据为QuerySet，不能Json化，我认为这个地方应该有更好的方式
    data_series_dict = {}
    for e in data_series:
        data_series_dict[e[0].strftime('%Y-%m-%d %H:%M:%S')] = round(e[1], 3)
    return JsonResponse(data_series_dict, safe=False)