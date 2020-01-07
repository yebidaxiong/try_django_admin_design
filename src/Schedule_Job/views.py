from django.shortcuts import render

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from django.db import connection

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# Create your views here.

@register_job(scheduler, 'cron', id='db_backup', day=15, hour=8, minute=30, args=['db_backup'])
def db_backup(s):
    # 这个地方要前台输入参数执行多久备份一次，并且备份执行过程中提示正在执行之类的,现在这个方式显然不好，因为会丢掉执行过程
    # 中的数据，想一下，如果前台的接口是从流引擎读，将写入和删除的时间交叉开，就不会出现这个问题，比如这五分钟并没有往里写
    print("schedule job is on...")
    cursor = connection.cursor()
    cursor.execute("SELECT NOW()")
    newest_record = cursor.fetchone()[0].strftime('%Y-%m-%d')
    query = "COPY(SELECT * FROM \"SMCS_SIS_REALTIME\") TO 'D:/SMCS_DB_BACKUP/smcs_sis_realtime_" + newest_record + ".json';"
    cursor.execute(query)
    query = "COPY(SELECT * FROM \"SMCS_SIS_Flag\") TO 'D:/SMCS_DB_BACKUP/smcs_sis_flag_" + newest_record + ".json';"
    cursor.execute(query)
    query = "COPY(SELECT * FROM \"SMCS_GAS_REALTIME\") TO 'D:/SMCS_DB_BACKUP/smcs_gas_realtime_" + newest_record + ".json';"
    cursor.execute(query)
    query = "COPY(SELECT * FROM \"SMCS_GAS_Flag\") TO 'D:/SMCS_DB_BACKUP/smcs_gas_flag_" + newest_record + ".json';"
    cursor.execute(query)

    query = "TRUNCATE TABLE \"SMCS_SIS_REALTIME\";"
    cursor.execute(query)
    query = "TRUNCATE TABLE \"SMCS_SIS_Flag\";"
    cursor.execute(query)
    query = "TRUNCATE TABLE \"SMCS_GAS_REALTIME\";"
    cursor.execute(query)
    query = "TRUNCATE TABLE \"SMCS_GAS_Flag\";"
    cursor.execute(query)


register_events(scheduler)
scheduler.start()
