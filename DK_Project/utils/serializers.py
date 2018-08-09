
"""

rest_framework  自定义序列化器

"""
import re
import json

from rest_framework import serializers

from market.models import Goods, GoodsBrand, GoodsCategory


class GoodSerializer(serializers.ModelSerializer):
    """自定义商品序列化器"""
    class Meta:
        model = Goods

    # 对获取到的数据进行数据格式化
    def to_representation(self, instance):
        data = super().to_representation(instance)
        category_id= data.pop('category')
        brand_id= data.pop('brand')
        product_info = data.pop('product_info')
        product_name = re.sub('分期乐', '简单贷', data.pop('product_name'))
        fe_params = json.loads(data.pop("fe_params"))
        slider_imgs = data.pop('slider_imgs').split('||')
        detail_imgs = data.pop('detail_imgs').split("||")
        data['category_id'] = category_id
        data['brand_id'] = brand_id
        data['product_info'] = product_info
        data['product_name'] = product_name
        data['fe_params'] = fe_params
        data['slider_imgs'] = slider_imgs
        data['detail_imgs'] = detail_imgs
        return data

    # def update(self, instance, validated_data):
    #     """
    #     重构数据结构
    #
    #     :param instance: 数据库中的数据
    #     :param validated_data:  更新后的数据
    #     :return:  处理后的结果状态码
    #     """
    #     instance.name = validated_data["name"]
    #     data = self.to_representation(instance)
    #     return {'code': 300, 'msg': '更新成功', 'data': 'data'}


class GoodsCategorySerializer(serializers.ModelSerializer):
    """商品种类序列化"""
    class Meta:
        model = GoodsCategory


class GoodsBrandSerializer(serializers.ModelSerializer):
    """商品的品牌序列化器"""
    class Meta:
        model = GoodsBrand
