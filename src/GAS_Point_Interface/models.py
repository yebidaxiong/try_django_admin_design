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
        db_table = "SMCS_GAS_Point_Reference"

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
        db_table = "SMCS_GAS_Category"

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
        db_table = "SMCS_GAS_DP_FE_ML"


class GASRealtime(models.Model):

    # 一个时间 TODO:
    add_time = models.DateTimeField(auto_now_add=True)
    point_1 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_2 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_3 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_4 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_5 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_6 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_7 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_8 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_9 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_10 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )

    point_11 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_12 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_13 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_14 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_15 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_16 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_17 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_18 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_19 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_20 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )

    point_21 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_22 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_23 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_24 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_25 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_26 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_27 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_28 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_29 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_30 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )

    point_31 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_32 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_33 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_34 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_35 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_36 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_37 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_38 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_39 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_40 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )

    point_41 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_42 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_43 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_44 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_45 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_46 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_47 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_48 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_49 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )
    point_50 = models.FloatField(default=0, blank=True, null=True, verbose_name="测点当前值", help_text="测点当前值", )

    class Meta:
        verbose_name = "GAS点实时数据"
        verbose_name_plural = verbose_name
        db_table = "SMCS_GAS_REALTIME"


class GASFlag(models.Model):

    # 一个时间 TODO:
    add_time = models.DateTimeField(auto_now_add=True)
    flag_1 = models.BooleanField(default=False, blank=True, null=True)
    flag_2 = models.BooleanField(default=False, null=True, blank=True)
    flag_3 = models.BooleanField(default=False, null=True, blank=True)
    flag_4 = models.BooleanField(default=False, null=True, blank=True)
    flag_5 = models.BooleanField(default=False, null=True, blank=True)
    flag_6 = models.BooleanField(default=False, null=True, blank=True)
    flag_7 = models.BooleanField(default=False, null=True, blank=True)
    flag_8 = models.BooleanField(default=False, null=True, blank=True)
    flag_9 = models.BooleanField(default=False, null=True, blank=True)
    flag_10 = models.BooleanField(default=False, null=True, blank=True)

    flag_11 = models.BooleanField(default=False, null=True, blank=True)
    flag_12 = models.BooleanField(default=False, null=True, blank=True)
    flag_13 = models.BooleanField(default=False, null=True, blank=True)
    flag_14 = models.BooleanField(default=False, null=True, blank=True)
    flag_15 = models.BooleanField(default=False, null=True, blank=True)
    flag_16 = models.BooleanField(default=False, null=True, blank=True)
    flag_17 = models.BooleanField(default=False, null=True, blank=True)
    flag_18 = models.BooleanField(default=False, null=True, blank=True)
    flag_19 = models.BooleanField(default=False, null=True, blank=True)
    flag_20 = models.BooleanField(default=False, null=True, blank=True)

    flag_21 = models.BooleanField(default=False, null=True, blank=True)
    flag_22 = models.BooleanField(default=False, null=True, blank=True)
    flag_23 = models.BooleanField(default=False, null=True, blank=True)
    flag_24 = models.BooleanField(default=False, null=True, blank=True)
    flag_25 = models.BooleanField(default=False, null=True, blank=True)
    flag_26 = models.BooleanField(default=False, null=True, blank=True)
    flag_27 = models.BooleanField(default=False, null=True, blank=True)
    flag_28 = models.BooleanField(default=False, null=True, blank=True)
    flag_29 = models.BooleanField(default=False, null=True, blank=True)
    flag_30 = models.BooleanField(default=False, null=True, blank=True)

    flag_31 = models.BooleanField(default=False, null=True, blank=True)
    flag_32 = models.BooleanField(default=False, null=True, blank=True)
    flag_33 = models.BooleanField(default=False, null=True, blank=True)
    flag_34 = models.BooleanField(default=False, null=True, blank=True)
    flag_35 = models.BooleanField(default=False, null=True, blank=True)
    flag_36 = models.BooleanField(default=False, null=True, blank=True)
    flag_37 = models.BooleanField(default=False, null=True, blank=True)
    flag_38 = models.BooleanField(default=False, null=True, blank=True)
    flag_39 = models.BooleanField(default=False, null=True, blank=True)
    flag_40 = models.BooleanField(default=False, null=True, blank=True)

    flag_41 = models.BooleanField(default=False, null=True, blank=True)
    flag_42 = models.BooleanField(default=False, null=True, blank=True)
    flag_43 = models.BooleanField(default=False, null=True, blank=True)
    flag_44 = models.BooleanField(default=False, null=True, blank=True)
    flag_45 = models.BooleanField(default=False, null=True, blank=True)
    flag_46 = models.BooleanField(default=False, null=True, blank=True)
    flag_47 = models.BooleanField(default=False, null=True, blank=True)
    flag_48 = models.BooleanField(default=False, null=True, blank=True)
    flag_49 = models.BooleanField(default=False, null=True, blank=True)
    flag_50 = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "GAS点实时报警"
        verbose_name_plural = verbose_name
        db_table = "SMCS_GAS_Flag"