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


# 这个地方先这么写，气体报警点名上来了再改
def get_gas_column_list(request):
    cursor = connection.cursor()
    cursor.execute("select COLUMN_NAME from information_schema.COLUMNS "
                   "where table_name = 'smcs_gas_realtime' and table_schema = 'smcs';")
    newest_record = cursor.fetchall()
    response_content = ()
    newest_record = newest_record[2:]
    for item in range(len(newest_record)):
        response_content += newest_record[item]
    return JsonResponse(response_content, safe=False)