from django.shortcuts import render
import json
import time
# Create your views here.

from django.http import JsonResponse
from django.db import connection


def get_gas_realtime_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_gas_realtime` where id = (SELECT MAX(id) FROM smcs_gas_realtime);")
    newest_record = cursor.fetchone()

    # 这个地方需要考证
    return JsonResponse(newest_record, safe=False)


def get_gas_flag_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `smcs_gas_flag` where id = (SELECT MAX(id) FROM smcs_gas_flag);")
    newest_record = cursor.fetchone()

    # 这个地方需要考证
    return JsonResponse(newest_record, safe=False)