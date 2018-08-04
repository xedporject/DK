from django.conf.urls import url
from DK_admin import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),  # 后端首页
    url(r'^top/', views.top, name='top'),  # 首页顶部
    url(r'^menu/', views.menu, name='menu'),  # 菜单栏
    url(r'^bar/', views.bar, name='bar'),  # 首页左边部分
    url(r'^main/', views.main, name='main'),  # 主页面
    url('^order_list/', views.order_list, name='order_list'),  # 订单页面
    url('^order_detail/', views.order_detail, name='order_detail'),  # 订单详情展示
    url('^get_order_info/', views.get_order_info, name='get_order_info'), # 订单信息展示接口
    url('^products/', views.products, name='products'),  # 商品展示
    url('^search_info/', views.search_info, name='search_info')  # 商品展示
]