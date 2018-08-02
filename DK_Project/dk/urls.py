from django.conf.urls import url

from dk import views

urlpatterns = [
   url(r'^home/',views.home,name='home')
]