from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
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
    # print(str(newest_record[1]))
    # 这个地方需要考证
    return JsonResponse(newest_record, safe=False)


def get_sis_flag_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_sis_flag` where id = (SELECT MAX(id) FROM smcs_sis_flag);")
    newest_record = cursor.fetchone()
    # 这个地方需要考证
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
    # 这个地方要根据发来的三个值把数据掐出来
    print(post_content['startTime'])
    print(post_content['endTime'])
    start_date = datetime.strptime(post_content['startTime'], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(post_content['endTime'], '%Y-%m-%d %H:%M:%S')
    print(type(start_date))
    print(type(end_date))
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    column_name = re.findall(p1, post_content['node'][0]['label'])[0]
    print(column_name)
    # print(column_name)
    # cursor = connection.cursor()
    # cursor.execute("select %s from smcs_sis_realtime where add_time between startTime and endTime"
    #                "values(%s, %s, %s)")
    # record = cursor.fetchall()
    # print(record)
    # 这个地方需要处理 其他地方没什么问题 TODO:这个地方需要处理 其他地方没什么问题
    result = models.SISRealtime.objects.values(column_name).filter(add_time__range=(start_date, end_date))
    # serialized_q = json.dumps(list(result), cls=DjangoJSONEncoder)
    print(result)
    return JsonResponse(result, safe=False)
