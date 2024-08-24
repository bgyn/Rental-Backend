from rest_framework import serializers
from api.models import (Category,)

class CategorySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"