from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from . serializers import *
from .models import *
# Create your views here.

class user(ListCreateAPIView):
    serializer_class = userserializer
    queryset = User.objects.all()

class user_detail_view(RetrieveAPIView):
    serializer_class = userserializer
    queryset = User.objects.all()

def home(request):
    return render(request, 'home.html')