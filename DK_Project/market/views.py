
from django.shortcuts import render
from rest_framework import mixins, viewsets

from market.models import Goods, GoodsCategory, GoodsBrand
from utils.serializers import GoodSerializer, GoodsBrandSerializer, GoodsCategorySerializer
from utils.filters import GoodsFilter, GoodsBrandFilter, GoodsCategoryFilter

# Create your views here.


def index(request):
    """商城首页"""
    return render(request, 'goods_market/index.html')


def detail(request):
    """商品详情页面"""
    return render(request, 'market/goods-detail.html')


def goods(request):
    """商品详细信息接口"""
    return


"""
    rest_framework  API 接口
"""


class GoodsApi(mixins.ListModelMixin,  # get
               mixins.CreateModelMixin,  # post
               mixins.RetrieveModelMixin,  # 单个查询
               mixins.UpdateModelMixin,  # 修改 put 全部  patch 部分
               mixins.DestroyModelMixin,  # 删除 delete
               viewsets.GenericViewSet):
    """商品 API """
    # 从数据库中获取的数据
    queryset = Goods.objects.filter(good_id__lt=200)
    # 数据序列化器, 将查询的数据进行处理,返回格式良好的数据
    serializer_class = GoodSerializer
    # 自定义的过滤器,对数据进行筛选
    filter_class = GoodsFilter


class BrandApi(mixins.ListModelMixin,  # get
               mixins.CreateModelMixin,  # post
               mixins.RetrieveModelMixin,  # 单个查询
               mixins.UpdateModelMixin,  # 修改 put 全部  patch 部分
               mixins.DestroyModelMixin,  # 删除 delete
               viewsets.GenericViewSet):
    """品牌的 API """
    queryset = GoodsBrand.objects.all()
    serializer_class = GoodsBrandSerializer
    filter_class = GoodsBrandFilter


class CategoryApi(mixins.ListModelMixin,  # get
               mixins.CreateModelMixin,  # post
               mixins.RetrieveModelMixin,  # 单个查询
               mixins.UpdateModelMixin,  # 修改 put 全部  patch 部分
               mixins.DestroyModelMixin,  # 删除 delete
               viewsets.GenericViewSet):
    """品牌的 API """
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer
    filter_class = GoodsCategoryFilter
