from django.shortcuts import render
import json
import time
# Create your views here.

from django.http import JsonResponse
from django.db import connection


# 这两个可以放在同一个请求里

def get_sis_realtime_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_sis_realtime` where id = (SELECT MAX(id) FROM smcs_sis_realtime);")
    newest_record = cursor.fetchone()
    # 这个地方需要考证
    return JsonResponse(newest_record, safe=False)


def get_sis_flag_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_sis_flag` where id = (SELECT MAX(id) FROM smcs_sis_flag);")
    newest_record = cursor.fetchone()
    # 这个地方需要考证
    return JsonResponse(newest_record, safe=False)
