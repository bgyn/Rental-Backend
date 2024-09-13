from rest_framework.serializers import ModelSerializer
from base.models import Categories


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id","category_name",]