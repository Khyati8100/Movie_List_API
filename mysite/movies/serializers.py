from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Moviedata
        fields = ['id','name','duration','rating','typ','image']