from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from food.models import Food, FoodCategory
from food.serializers import FoodListSerializer


class FoodModelViewSet(ModelViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = (
            FoodCategory.objects.filter(food__is_publish=True)
            .prefetch_related(
                Prefetch("food", queryset=Food.objects.filter(is_publish=True))
            )
            .distinct()
            .order_by("id")
        )
        return queryset
