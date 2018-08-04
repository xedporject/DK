from django.conf.urls import url
from DK_home import views

urlpatterns = [
    url('^index/',views.index,name='index')
]