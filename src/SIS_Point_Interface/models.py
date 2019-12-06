from django.db import models

# Create your models here.
from Abstract_Base_Interface.models import PointBase, CategoryBase


class SISPoint(PointBase):
    """
    SIS point attribute references
    """
    is_tab = models.BooleanField(default=False)

    class Meta:
        verbose_name = "SIS测点属性表"
        verbose_name_plural = verbose_name
        db_table = "SCMS_SIS_Point_Reference"


class SISPointCategory(CategoryBase):
    """
    SIS point category attribute references, means SIS point belong to which area, opc, or computer
    """
    SIS_CATEGORY_TYPE = (
        (1, "SIS一级类别"),
        (2, "SIS二级类别"),
        (3, "SIS三级类别"),
        (4, "SIS四级类别"),
    )

    SIS_category_type = models.IntegerField(choices=SIS_CATEGORY_TYPE, verbose_name="SIS类别分类", help_text="SIS类别分类")
    is_tab = models.BooleanField(default=False)

    class Meta:
        verbose_name = "SIS测点分类"
        verbose_name_plural = verbose_name
        db_table = "SCMS_SIS_Category"


class SISPointOnMapping(models.Model):
    """
    This is a very important table stores relationships to SIS point from DCS points and also SIS GAS, one-many,
    for offline data processing, feature engineering, and online ML model running
    """
    SIS_point_code = models.CharField()
    DCS_point_code = models.CharField()
    # according to model selection, there may be several kinds of correlation weight, not sure about this.
    # Random Forest has no weights.
    correlation_weight = models.FloatField()

    class Meta:
        verbose_name = "SIS目标点的特征映射"
        verbose_name_plural = verbose_name
        db_table = "SCMS_SIS_DP_FE_ML"
