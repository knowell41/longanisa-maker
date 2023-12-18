from .models import *
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate, get_user_model


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = "__all__"
