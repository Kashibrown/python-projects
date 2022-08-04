from rest_framework import serializers
from core.models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__' 