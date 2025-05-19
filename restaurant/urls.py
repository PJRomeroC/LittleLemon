#define URL route for index() view
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu-items'),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="menu-item-detail"),
]
