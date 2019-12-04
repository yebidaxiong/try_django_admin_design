from django.db import models

# Create your models here.
from Abstract_Base_Interface.models import PointBase, CategoryBase


class GASPoint(PointBase):
    """
    GAS point attribute references
    """
    is_tab = models.BooleanField(default=False)

    class Meta:
        verbose_name = "GAS测点属性表"
        verbose_name_plural = verbose_name
        db_table = "SCMS_GAS_Point_Reference"


class GASPointCategory(CategoryBase):
    """
    GAS point category attribute references, means GAS point belong to which area, opc, or computer
    """
    GAS_CATEGORY_TYPE = (
        (1, "GAS一级类别"),
        (2, "GAS二级类别"),
        (3, "GAS三级类别"),
        (4, "GAS四级类别"),
    )

    GAS_category_type = models.IntegerField(choices=GAS_CATEGORY_TYPE, verbose_name="GAS类别分类", help_text="GAS类别分类")
    is_tab = models.BooleanField(default=False)

    class Meta:
        verbose_name = "GAS测点分类"
        verbose_name_plural = verbose_name
        db_table = "SCMS_GAS_Category"