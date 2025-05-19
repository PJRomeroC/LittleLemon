#define URL route for index() view
from django.urls import path
from .views import MenuItemView, SingleMenuItemView,RegisterUserView, index
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu-items/', MenuItemView.as_view(), name='menu-items'),
    path("menu-items/<int:pk>", SingleMenuItemView.as_view(), name="menu-item-detail"),
    path('api-token-auth/', obtain_auth_token, name='user-login'),
    path('registration/', RegisterUserView.as_view(), name='user-register')
]
