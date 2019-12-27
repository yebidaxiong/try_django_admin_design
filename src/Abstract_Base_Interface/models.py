from datetime import datetime

from django.db import models

"""
Please remember, currently there is no tables about image or video live stream processing
"""


# Create your models here.

class CategoryBase(models.Model):
    """
    category base class, for DCS, SIS, GAS point and Camera Category class to inherit, no table built.
    """
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(default="", max_length=30, blank=True, verbose_name="分类名", help_text="分类名")
    category_code = models.CharField(default="", max_length=30, blank=True, verbose_name="分类code", help_text="分类code")
    category_desc = models.TextField(default="", blank=True, verbose_name="分类描述", help_text="分类描述")
    # category_type = models.CharField() # write here just for remind, should be in each class object
    # each point DCS, SIS, GAS has their own category type
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    # is_tab = models.BooleanField(default=False) DCS has no is_tab, SIS and GAS has is_tab

    add_time = models.DateTimeField(default=datetime.now, blank=True, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        abstract = True


class PointBase(models.Model):
    """
    point base class, for DCS, SIS, GAS point class to inherit, no table built.
    """
    # point attributes
    id = models.AutoField(primary_key=True)
    point_name = models.CharField(default="", max_length=30, blank=True, verbose_name="测点名称", help_text="测点名称")
    point_code = models.CharField(default="", max_length=30, blank=True, verbose_name="测点位号", help_text="测点位号")
    point_desc = models.TextField(default="", blank=True, verbose_name="测点描述", help_text="测点描述")
    point_category = models.CharField(default="", max_length=30, blank=True,
                                      verbose_name="测点所属类别", help_text="测点所属类别")
    point_unit = models.CharField(default="", max_length=30, blank=True, verbose_name="测量单位", help_text="测量单位")

    # flag of opc connection(cannot edit in admin， edit by opc readers)
    point_connection_status = models.BooleanField(default=False, blank=True, editable=False,
                                                  verbose_name="测点连接状况", help_text="测点连接状况")

    # flag of added to dynamic card board(cannot edit in admin, edit by dynamic card board)
    is_tab = models.BooleanField(default=False, blank=True, editable=False,
                                 verbose_name="测点添加到动态卡片板", help_text="测点添加到动态卡片板")

    # flag of offering service to app(cannot edit in admin, edit by some other item)
    point_add_to_service = models.BooleanField(default=False, blank=True, editable=False,
                                               verbose_name="测点添加到服务", help_text="测点添加到服务")
    # point value related
    point_H_limitation = models.FloatField(default=0, blank=True, verbose_name="测点上限", help_text="测点上限", )
    point_L_limitation = models.FloatField(default=0, blank=True, verbose_name="测点下限", help_text="测点下限", )
    point_HH_limitation = models.FloatField(default=0, blank=True, verbose_name="测点上上限", help_text="测点上上限", )
    point_LL_limitation = models.FloatField(default=0, blank=True, verbose_name="测点下下限", help_text="测点下下限", )
    point_realtime_value = models.FloatField(default=0, blank=True, verbose_name="测点当前值", help_text="测点当前值", )

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    # point_camera_bind = models.URLField()  # wish to bind cameras to point, one point has several cameras, but need
    # another table

    class Meta:
        abstract = True


class CameraBase(models.Model):
    """
    camera base class, for camera class to inherit, no table built.
    """
    id = models.AutoField(primary_key=True)
    camera_name = models.CharField(default="", max_length=30, blank=True, verbose_name="摄像头名称", help_text="摄像头名称")
    camera_url = models.URLField(default="", max_length=200, blank=True, verbose_name="摄像头位号", help_text="摄像头位号")
    camera_category = models.CharField(default="", max_length=30, blank=True, verbose_name="摄像头类别", help_text="摄像头类别")
    camera_desc = models.TextField(default="", blank=True, verbose_name="摄像头描述", help_text="摄像头描述")
    camera_connection_status = models.BooleanField(default=True, blank=True, verbose_name="摄像头连接状态",
                                                   help_text="摄像头连接状态")
    add_time = models.DateTimeField(default=datetime.now, blank=True, verbose_name="添加时间", help_text="添加时间")

    #  camera_initial_image = models.ImageField()

    class Meta:
        abstract = True


class EventBase(models.Model):
    """
    event abstract base class, for event class to inherit, problem is I just put it here, not expect used, because
    event has many sources and restrictions, need to analyze carefully, no table built.
    """
    id = models.AutoField(primary_key=True)
    event_source = models.CharField(max_length=30, verbose_name="事件源", help_text="事件源")
    event_type = models.CharField(max_length=30, verbose_name="事件类型", help_text="事件类型")
    event_happened_time = models.DateTimeField(verbose_name="事件发生时间", help_text="事件发生时间")  # this is add time I suppose
    event_detail_desc = models.TextField(verbose_name="事件详细信息", help_text="事件详细信息")
    event_status = models.BooleanField(default=False, verbose_name="事件状态", help_text="事件状态")
    event_level = models.IntegerField(verbose_name="事件级别", help_text="事件级别")
    event_analysis = models.TextField(verbose_name="事件分析", help_text="事件分析")

    # is_tab = models.BooleanField(default=False, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        abstract = True


class FlagBase(models.Model):
    """
    flag base class, for inherit, maybe not used
    """
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        abstract = True


class LogBase(models.Model):
    """
    Log base class
    """
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        abstract = True
