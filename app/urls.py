from django.urls import path, include
from rest_framework_nested import routers

from repertoire import views

router = routers.SimpleRouter()
router.register(r'countries', views.CountryViewSet, basename='countries')

files_router = routers.NestedSimpleRouter(router, r"countries", lookup='country')
files_router.register(r'stores', views.StoreViewSet, basename='countrystores')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(files_router.urls)),
]
