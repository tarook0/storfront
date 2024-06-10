from django.urls import path
from . import views
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register('products', viewset=views.ProductViewSet ,basename='products')
router.register('collections', viewset=views.CollectionViewSet)
produccts_router=routers.NestedDefaultRouter(router,'products',lookup='product')
produccts_router.register('reviews',views.ReviewViewSet,basename='products-reviews')
# URLConf
urlpatterns = router.urls+produccts_router.urls
