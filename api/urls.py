from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LostItemsViewset, FoundItemViewset
from . import views
router = DefaultRouter()
router.register(r"lost-items", views.LostItemsViewset, basename='lostitems')
router.register(r"found-items", views.FoundItemViewset, basename='founditem')
urlpatterns = [
    path('', include(router.urls)),
  
    
]