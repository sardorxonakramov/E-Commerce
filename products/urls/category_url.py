from django.urls import path

from products.views.category import (
    CategoryCreateView,
    CategoryListView,
    CategoryRetrieveView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("<int:pk>/", CategoryRetrieveView.as_view(), name="category-retrieve"),
    path("create/", CategoryCreateView.as_view(), name="category-create"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
]

# Raw data bo'yicha berish kerak cretaeda
# {
#   "category": 2,
#   "name":"Tashqi kiyim",
#   "description":"Yuqori sifatli matodan",
#   "price": "450000.00",
#   "is_top": false,
#   "stock": 25,
#   "images": [
#     {
#       "image_id": 1,
#       "is_main": true
#     },
#     {
#       "image_id": 2,
#       "is_main": false
#     }
#   ]
# }
# ------------crud-----------


# {
#   "name": {
#     "uz": "Yangilangan nom",
#     "ru": "Новое имя",
#     "en": "Updated Name"
#   },
#   "description": {
#     "uz": "Tavsif",
#     "ru": "Описание",
#     "en": "Description"
#   },
#   "price": "199000.00",
#   "stock": 7,
#   "is_top": true,
#   "images": [
#     {"upload_id": 12, "is_main": true},
#     {"upload_id": 14, "is_main": false}
#   ]
# }
