
import django_filters
from rest_framework import filters

from market.models import Goods, GoodsBrand, GoodsCategory


class GoodsFilter(filters.FilterSet):
    """用于商品查询的过滤器"""
    class Meta:
        model = Goods
        # 用于查询的字段
        fields = '__all__'

    # 定义查询的方法 contains:模糊查询; gte:大于等于; lte:小于等于
    # url : /market/goods/?good_id_lte=160&  添加其他条件
    good_id = django_filters.CharFilter('good_id', lookup_expr='exact')
    good_id_lte = django_filters.CharFilter('good_id', lookup_expr='lte')
    good_id_gte = django_filters.CharFilter('good_id', lookup_expr='gte')
    good_name = django_filters.CharFilter('good_name', lookup_expr='icontains')
    good_category_id = django_filters.CharFilter('category_id', lookup_expr='exact')
    good_brand_id = django_filters.CharFilter('brand_id', lookup_expr='exact')
    good_amount_lte = django_filters.CharFilter("real_amount", lookup_expr='lte')
    good_amount_gte = django_filters.CharFilter("real_amount", lookup_expr='gte')


class GoodsBrandFilter(filters.FilterSet):
    """查询品牌的过滤器"""
    class Meta:
        model = GoodsBrand
        fields = "__all__"
    # 定义查询字段
    brand_id = django_filters.CharFilter('brand_id', lookup_expr='exact')
    brand_name = django_filters.CharFilter('brand_name', lookup_expr='icontains')
    brand_category_id = django_filters.CharFilter("category_id_1", lookup_expr='exact')


class GoodsCategoryFilter(filters.FilterSet):
    """查询分类的过滤器"""
    class Meta:
        model = GoodsCategory
        fields = '__all__'

    category_id = django_filters.CharFilter("category_id", lookup_expr='exact')
    category_name = django_filters.CharFilter('category_name', lookup_expr='icontains')

