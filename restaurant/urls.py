#define URL route for index() view
from django.urls import path
from .views import MenuItemView, SingleMenuItemView, index
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu-items'),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="menu-item-detail"),
    path('api-token-auth/', obtain_auth_token),
]
