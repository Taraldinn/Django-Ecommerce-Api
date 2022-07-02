from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers
# URLConf

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
urlpatterns = router.urls + products_router.urls
