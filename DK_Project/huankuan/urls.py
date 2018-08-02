from django.conf.urls import url

from huankuan import views

urlpatterns = [
    url(r'^order_detail/', views.order_detail, name='order_detail'),

]