from datetime import datetime

from django.db import models

# Create your models here.
from Abstract_Base_Interface.models import PointBase, CategoryBase


class DCSPoint(PointBase):
    """
    DCS point attribute references
    """

    class Meta:
        verbose_name = "DCS测点属性"
        verbose_name_plural = verbose_name
        db_table = "SMCS_DCS_Point_Reference"

    # def __str__(self):
    #     return PointBase.point_name


class DCSPointCategory(CategoryBase):
    """
    DCS point category attribute references, means DCS point belong to which area, opc, or computer
    """
    DCS_CATEGORY_TYPE = (
        (1, "DCS一级类别"),
        (2, "DCS二级类别"),
        (3, "DCS三级类别"),
        (4, "DCS四级类别"),
    )

    DCS_category_type = models.IntegerField(choices=DCS_CATEGORY_TYPE, verbose_name="DCS类别分类", help_text="DCS类别分类")

    class Meta:
        verbose_name = "DCS测点分类"
        verbose_name_plural = verbose_name
        db_table = "SMCS_DCS_Category"

    def __str__(self):
        return CategoryBase.category_name