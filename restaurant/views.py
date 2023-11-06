from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from .models import Booking, MenuItem
from django.contrib.auth.models import User

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 
        
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated] 
    class Meta:
        model = MenuItem
        fields = '__all__'

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})