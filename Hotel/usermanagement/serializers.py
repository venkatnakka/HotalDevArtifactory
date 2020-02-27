from rest_framework.serializers import ModelSerializer
from .models import *
class userserializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"