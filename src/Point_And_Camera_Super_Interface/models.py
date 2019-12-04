from django.db import models


# Create your models here.

class PointCategory(models.Model):
    """
    测点类别父类，用于给DCS，SIS，GAS测点继承，不生成表
    """

    class Meta:
        # 表示我是抽象类，只用于继承，不在MySQL生成表
        abstract = True


class Point(models.Model):
    """
    测点父类，用于给DCS，SIS，GAS测点继承，不生成表
    """
    class Meta:
        abstract = True


class CameraCategory(models.Model):
    """
    摄像头类别父类，用于给DCS，SIS，GAS测点继承，不生成表
    """
    class Meta:
        abstract = True


class Camera(models.Model):
    """
    摄像头父类，用于给DCS，SIS，GAS测点继承，不生成表
    """
    class Meta:
        abstract = True
