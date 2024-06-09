from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('products', viewset=views.ProductViewSet)
router.register('collections', viewset=views.CollectionViewSet)
# URLConf
urlpatterns = router.urls
