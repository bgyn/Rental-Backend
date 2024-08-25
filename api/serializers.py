from rest_framework import serializers
from api.models import (Category,RentList)

class CategorySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class RentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentList
        fields = "__all__"