from django.urls import include, path
from rest_framework.routers import DefaultRouter

from food.views import FoodModelViewSet

app_name = "food"
router = DefaultRouter()
router.register(r"foods", FoodModelViewSet, basename="Food")
urlpatterns = [path("", include(router.urls))]
