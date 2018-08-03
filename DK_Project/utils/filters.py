
import django_filters
from rest_framework import filters

from market.models import Goods, GoodsBrand, GoodsCategory


class GoodsFilter(filters.FilterSet):
    """用于商品查询的过滤器"""
    class Meta:
        model = Goods
        # 用于查询的字段
        fields = ('good_id', 'good_name', 'category_id', 'brand_id')

    # 定义查询的方法 contains:模糊查询; gte:大于等于; lte:小于等于
    # url : /market/goods/?good_id_lte=160
    good_id_lte = django_filters.CharFilter('good_id', lookup_expr='lte')
    good_id_gte = django_filters.CharFilter('good_id', lookup_expr='gte')
    good_name = django_filters.CharFilter('good_name', lookup_expr='contains')
    # good_category_id = django_filters.CharFilter('category_id', lookup_expr='')
    # good_brand_id = django_filters.CharFilter('brand_id', lookup_expr='')


class GoodsBrandFilter(filters.FilterSet):
    """查询品牌的过滤器"""
    class Meta:
        model = GoodsBrand
        fields = ('brand_id', 'brand_name')

    # 定义查询方法
    brand_id_lte = django_filters.CharFilter('brand_id', lookup_expr='lte')
    brand_id_gte = django_filters.CharFilter('brand_id', lookup_expr='gte')
    brand_name = django_filters.CharFilter('brand_name', lookup_expr='contains')
