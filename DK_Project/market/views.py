from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'market/uc.html')


def detail(request):
    """商品详情页面"""
    return render(request, 'market/goods-detail.html')