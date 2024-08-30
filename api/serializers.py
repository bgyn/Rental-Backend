from rest_framework import serializers
from api.models import (Category,RentList)

class CategorySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class RentListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = RentList
        fields = "__all__"

    def get_images(self,obj):
        return [image.image.url for image in obj.images.all()]