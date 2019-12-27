from django.contrib import admin

# Register your models here.
from DCS_Point_Interface.models import DCSPoint, DCSPointCategory

admin.site.register(DCSPoint)
admin.site.register(DCSPointCategory)