from django.contrib import admin

from GAS_Point_Interface.models import GASPoint, GASPointCategory, GASPointOnMapping, GASRealtime, GASFlag
# Register your models here.


admin.site.register(GASPoint)
admin.site.register(GASPointCategory)
admin.site.register(GASPointOnMapping)
admin.site.register(GASRealtime)
admin.site.register(GASFlag)