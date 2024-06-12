from django.urls import path
from . import views
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register('products', viewset=views.ProductViewSet, basename='products')
router.register('collections', viewset=views.CollectionViewSet)
router.register('carts', viewset=views.CartViewset)
router.register('customers', viewset=views.CustomerViewSet)
produccts_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
produccts_router.register(
    'reviews', views.ReviewViewSet, basename='products-reviews')
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewset, basename='cart_items')

# URLConf
urlpatterns = router.urls+produccts_router.urls+carts_router.urls
