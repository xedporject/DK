from django.shortcuts import render,HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from DK_home.models import *
# Create your views here.


def index(request):
    """后端首页"""
    if request.method == 'GET':
        return render(request, 'admin/index.html')


def top(request):
    """首页顶部"""
    if request.method == 'GET':
        return render(request,'admin/top.html')


def bar(request):
    """首页左边部分"""
    if request.method == 'GET':
        return render(request,'admin/bar.html')


def menu(request):
    """菜单栏"""
    if request.method == 'GET':
        return render(request,'admin/menu.html')


def main(request):
    """主页面"""
    if request.method == 'GET':
        return render(request,'admin/main.html')


def order_list(request):
    """订单页面"""
    if request.method == 'GET':
        return render(request,'admin/order_list.html')


def get_order_info(request):
    """订单展示接口"""
    if request.method == 'GET':
        users = UserTable.objects.all()
        user_list = [user.to_dict() for user in users]
        data = {'user_list': user_list}
        return JsonResponse(data)


def order_detail(request):
    """订单展示页面"""
    if request.method == 'GET':
        id = request.GET.get('id')
        user = UserTable.objects.filter(user_id=id)
        return render(request, 'admin/order_detail.html')


def products(request):
    """商品展示"""
    if request.method == 'GET':

        products = Products.objects.filter(product_id=1)
        product_info = [product.to_dict() for product in products]
        product_msg = {
            'code': 200,
            'product_info': product_info
        }
        return JsonResponse(product_msg)


def search_info(request):
    """查询"""
    if request.method == 'GET':
        # 订单号
        loan_id = request.GET.get('loan_id')
        # 身份证号
        user_card = request.GET.get('user_card')
        # 用户
        name = request.GET.get('user_name')
        # 时间
        pri_date = request.GET.get('pri_date')
        # 是否处理
        do = request.GET.get('do_')
        # 现金贷&pos贷
        loan_name = request.GET.get('way')
        select_dict = dict()
        if loan_id:
            select_dict['loan_id'] = loan_id
        if user_card:
            select_dict['user_card'] = user_card
        if name:
            select_dict['name'] = name
        if pri_date:
            select_dict['pri_date'] = pri_date
        if do:
            statu_info = StatuTable.objects.filter(statu_name=do).first()
            select_dict['statu_id'] = statu_info.statu_id
        if loan_name:
            loa_loan = LoantypeTable.objects.filter(loan_name=loan_name).first()
            select_dict['loa_loan_id'] = loa_loan.loan_id
        # 多条件查询
        user_table_list = UserTable.objects.filter(**select_dict)
        data_info = [user_table.to_dict() for user_table in user_table_list]
        data = {
            'code': 200,
            'data_info': data_info
        }
        # 返回json数据
        return JsonResponse(data)
