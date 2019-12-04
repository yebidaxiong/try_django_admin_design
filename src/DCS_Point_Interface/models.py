from datetime import datetime

from django.db import models


# Create your models here.

class DcsCategory(models.Model):
    """
    DCS测点类别,用一个类定义循环类别，由用户自己定义一个DCS测点上层有几个类别，比如作业区-设备-测点等等，
    """
    CATEGORY_TYPE = (
        (1, ""),
        (2, ""),
        (3, ""),
    )

    name = models.CharField(default="", max_length=50, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")  # 用来说明这个类是哪个级别的类
    category_type = models.CharField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别")

    # 是否放入主预览界面
    is_tab = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "DCS测点类别"
        verbose_name_plural = verbose_name
