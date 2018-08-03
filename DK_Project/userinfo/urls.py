from django.conf.urls import url


from userinfo import views

urlpatterns = [
    url(r'^true_info/', views.true_info, name='tinfo')
]