
"""

rest_framework  自定义序列化器

"""

from rest_framework import serializers

from market.models import Goods, GoodsBrand, GoodsCategory


class GoodSerializer(serializers.ModelSerializer):
    """自定义商品序列化器"""
    class Meta:
        model = Goods

    # def to_representation(self, instance):
    #     """对对查询到的对象 instance 进行初步的处理, 如可以将外键的一些属性进行查询"""
    #     data = super().to_representation(instance)
    #     data['name'] = instance.fk.name
    #     return data
    #
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
