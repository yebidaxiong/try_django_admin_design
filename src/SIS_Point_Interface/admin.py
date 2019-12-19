from django.contrib import admin

from SIS_Point_Interface.models import SISPoint, SISPointCategory, SISPointOnMapping, SISRealtime, SISFlag
# Register your models here.


admin.site.site_title = "安全预警后台管理"
admin.site.site_header = "安全预警管理后台"

admin.site.register(SISPoint)
admin.site.register(SISPointCategory)
admin.site.register(SISPointOnMapping)
admin.site.register(SISRealtime)
admin.site.register(SISFlag)