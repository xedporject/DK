# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class GoodsCategory(models.Model):
    category_id = models.IntegerField(primary_key=True, null=True)
    category_name = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'goods_category'


class GoodsBrand(models.Model):
    brand_id = models.IntegerField(primary_key=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=32, blank=True, null=True)
    brand_name_ch = models.CharField(max_length=32, blank=True, null=True)
    brand_name_en = models.CharField(max_length=32, blank=True, null=True)
    category = models.ForeignKey('GoodsCategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'goods_brand'


class Goods(models.Model):
    good_id = models.AutoField(primary_key=True, null=True)
    good_name = models.CharField(max_length=32, blank=True, null=True)
    category = models.ForeignKey('GoodsCategory', models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey('GoodsBrand', models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    short_product_name = models.CharField(max_length=32, blank=True, null=True)
    sku_key_1 = models.CharField(max_length=32, blank=True, null=True)
    sku_key_2 = models.CharField(max_length=32, blank=True, null=True)
    sku_key_3 = models.CharField(max_length=32, blank=True, null=True)
    product_flag = models.IntegerField()
    min_firstpay = models.IntegerField(blank=True, null=True)
    is_product_up_down = models.IntegerField(blank=True, null=True)
    real_amount = models.IntegerField(blank=True, null=True)
    mart_amount = models.IntegerField(blank=True, null=True)
    fq_num = models.IntegerField(blank=True, null=True)
    product_info = models.CharField(max_length=100, blank=True, null=True)
    delivery_time = models.CharField(max_length=64, blank=True, null=True)
    gift_list = models.CharField(max_length=200, blank=True, null=True)
    fe_params = models.TextField(blank=True, null=True)
    slider_imgs = models.TextField(blank=True, null=True)
    detail_imgs = models.TextField(blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'goods'

