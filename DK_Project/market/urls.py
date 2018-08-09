
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from market import views


router = SimpleRouter()
router.register(r'^goods', views.GoodsApi)
router.register(r'brand', views.BrandApi)
router.register(r'category', views.CategoryApi)

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'goods/details/(\d+)/', views.details)
]
urlpatterns += router.urls
