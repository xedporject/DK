
from __future__ import unicode_literals

import json

from django.db import models


class GoodsCategory(models.Model):

    class Meta:
        db_table = 'goods_category'

    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)


class GoodsBrand(models.Model):

    class Meta:
        db_table = 'goods_brand'

    brand_id = models.IntegerField(primary_key=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=32, blank=True, null=True)
    brand_name_ch = models.CharField(max_length=32, blank=True, null=True)
    brand_name_en = models.CharField(max_length=32, blank=True, null=True)
    category = models.ForeignKey('GoodsCategory', models.DO_NOTHING, blank=True, null=True)


class Goods(models.Model):

    class Meta:
        db_table = 'goods'

    good_id = models.AutoField(primary_key=True)
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

    def to_dict(self):
        self.slider_imgs = self.slider_imgs.split("||")
        self.detail_imgs = self.detail_imgs.split("||")
        self.fe_params = json.loads(self.fe_params)
        return {
            "good_id": self.good_id,
            "good_name": self.good_name,
            "category_id": self.category_id,
            "brand_id": self.brand_id,
            "sku_key_1": self.sku_key_1,
            "sku_key_2": self.sku_key_2,
            "sku_key_3": self.sku_key_3,
            "real_amount": self.real_amount,
            "mart_amount": self.mart_amount,
            "slider_imgs": self.slider_imgs,
            "detail_imgs": self.detail_imgs,
        }






