from django.urls import path
from .views import shopping_page, detail


urlpatterns = [
    path('', shopping_page),
    path('<my_id>/', detail),
]
