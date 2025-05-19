from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
     queryset = MenuItem.objects.all()
     serializer_class = MenuSerializer
     permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
     queryset = MenuItem.objects.all()
     serializer_class = MenuSerializer
     permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
     queryset = Booking.objects.all()
     serializer_class = BookingSerializer
     permission_classes = [IsAuthenticated]

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)