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
    category_name = models.CharField(default="", max_length=30, verbose_name="分类名", help_text="分类名")
    category_code = models.CharField(default="", max_length=30, verbose_name="分类code", help_text="分类code")
    category_desc = models.TextField(default="", verbose_name="分类描述", help_text="分类描述")
    # category_type = models.CharField() # write here just for remind, should be in each class object
    # each point DCS, SIS, GAS has their own category type
    parent_category = models.ForeignKey("self", null=True, verbose_name="父类目级", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    # is_tab = models.BooleanField(default=False) DCS has no is_tab, SIS and GAS has is_tab

    add_time = models.DateTimeField(datetime.now(), verbose_name="添加时间")

    class Meta:
        abstract = True


class PointBase(models.Model):
    """
    point base class, for DCS, SIS, GAS point class to inherit, no table built.
    """
    id = models.AutoField(primary_key=True)
    point_name = models.CharField()
    point_code = models.CharField()
    # point_category = models.CharField()
    point_desc = models.TextField()
    point_connection_status = models.BooleanField(default=True)  # flag of opc connection
    point_add_to_service = models.BooleanField(default=False)  # flag of offering service to app
    point_H_limitation = models.FloatField()
    point_L_limitation = models.FloatField()
    point_HH_limitation = models.FloatField()
    point_LL_limitation = models.FloatField()

    add_time = models.DateTimeField()

    # point_camera_bind = models.URLField()  # wish to bind cameras to point, one point has several cameras, but need
    # another table

    class Meta:
        abstract = True


class CameraBase(models.Model):
    """
    camera base class, for camera class to inherit, no table built.
    """
    id = models.AutoField(primary_key=True)
    camera_name = models.CharField()
    camera_url = models.URLField(max_length=200)
    camera_category = models.CharField()
    camera_desc = models.TextField()
    camera_connection_status = models.BooleanField(default=True)
    add_time = models.DateTimeField()

    #  camera_initial_image = models.ImageField()

    class Meta:
        abstract = True


class EventBase(models.Model):
    """
    event abstract base class, for event class to inherit, problem is I just put it here, not expect used, because
    event has many sources and restrictions, need to analyze carefully, no table built.
    """
    id = models.AutoField(primary_key=True)
    event_source = models.CharField()
    event_type = models.CharField()
    event_happened_time = models.DateTimeField()  # this is add time I suppose
    event_detail_desc = models.TextField()
    event_status = models.BooleanField(default=False)
    event_level = models.IntegerField()
    event_analysis = models.TextField()
    is_tab = models.BooleanField(default=False)

    class Meta:
        abstract = True


class FlagBase(models.Model):
    """
    flag base class, for inherit, maybe not used
    """
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField()

    class Meta:
        abstract = True


class LogBase(models.Model):
    """
    Log base class
    """
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField()

    class Meta:
        abstract = True


