from django.urls import path
from .views import shopping_page, detail  # categories


urlpatterns = [
    path('', shopping_page),
    path('<my_id>/', detail),
    #path('<make>/', categories),
]
