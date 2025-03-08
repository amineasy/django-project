from rest_framework import serializers
from .models import *


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    music_related = MusicSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
