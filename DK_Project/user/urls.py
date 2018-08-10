from django.conf.urls import url

from user import views

urlpatterns=[
    url(r'^user_register/', views.user_register, name='user_register'),
    url(r'^user_code/', views.code, name='user_code'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^index',views.index,name='index'),
    url(r'^edit_password',views.edit_password,name='edit_password'),
    url(r'^user_logout',views.user_logout,name='user_logout')

]