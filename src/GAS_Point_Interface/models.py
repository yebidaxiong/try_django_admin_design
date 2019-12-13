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

        def __str__(self):
            return PointBase.point_name


class GASPointCategory(CategoryBase):
    """
    GAS point category attribute references, means GAS point belong to which area, opc, or computer
    """

    # this should be defined by customers, factories,
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

    def __str__(self):
        return CategoryBase.category_name


class GASPointOnMapping(models.Model):
    """
    This is a very important table stores relationships to GAS point from DCS points and also SIS GAS, one-many,
    for offline data processing, feature engineering, and online ML model running
    """

    GAS_point_code = models.CharField(max_length=30)
    DCS_point_code = models.CharField(max_length=30)
    # according to model selection, there may be several kinds of correlation weight, not sure about this.
    # Random Forest has no weights.
    correlation_weight = models.FloatField()

    class Meta:
        verbose_name = "GAS目标点的特征映射"
        verbose_name_plural = verbose_name
        db_table = "SCMS_GAS_DP_FE_ML"

