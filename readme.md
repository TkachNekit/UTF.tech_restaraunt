# Тестовое задание: Backend разработчик в UTF.tech
## Описание
Тестовое задание представляет собой создание API для получения информации о блюдах ресторана по категориям.

##  Стек технологий
- Django
- Django REST Framework (DRF)
## Задача
Даны модели "Категория Блюд" и "Блюдо" для ресторана. Требуется написать view, который вернет информацию о блюдах в формате JSON следующего вида:
```json
[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 100,
                "code": 1,
                "name_ru": "Чай",
                "description_ru": "Чай 100 гр",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [
                    200
                ]
            },
            ...
        ]
    },
    ...
]
```
## Условия
- В выборку попадают только блюда, у которых is_publish=True.
- Если в категории нет блюд (или все блюда данной категории имеют is_publish=False), то такая категория не включается в выборку.
- Запрос к базе данных должен быть выполнен любым удобным способом: Django ORM (предпочтительно), Raw SQL, SQLAlchemy и т.д.

## Написанный View
```python
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
```

## Использование
1. Склонируйте репозиторий 
```text
git clone https://github.com/TkachNekit/UTF.tech_restaraunt
```

2. Создайте виртуальное окружение
```text
python -m venv ../venv
source ../venv/bin/activate
```

3. Убедитесь, что у вас установлены все зависимости.
```text
pip install --upgrade pip
pip install -r requirements.txt
```
4. Создайте .env файл
```text
DEBUG=bool
SECRET_KEY=django_secret_key
```

5. Примените миграции и при помощи фикстур наполните БД
```text
python manage.py migrate
python manage.py loaddata fixtures/data.json
```

6. Запустите сервер Django.
```text
python manage.py runserver 
```
7. Перейдите по адресу для получения списка блюд в формате JSON.
```text
 http://127.0.0.1:8000/api/v1/foods/
 ```
