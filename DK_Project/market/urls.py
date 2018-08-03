
from django.conf.urls import url

from market import views


urlpatterns = [
    url(r'^index/', views.index, name='index')
]