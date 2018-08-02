from django.conf.urls import url

from dk_admin import views

urlpatterns = [
    url(r'^$', views.admin, name='admin'),
    url(r'^top/', views.top, name='top'),
    url(r'^bar/', views.bar, name='bar'),
    url(r'^menu/', views.menu, name='menu'),
    url(r'^main/', views.main, name='main'),
    url(r'^order_list/', views.order_list, name='order_list'),
]
