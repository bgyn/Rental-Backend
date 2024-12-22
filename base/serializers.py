from rest_framework import serializers
from base.models import Categories,Rules,RentItem,User,UserListing

class RentItemSerializer(serializers.ModelSerializer):
    itemRules = serializers.SerializerMethodField(read_only = True)
    category = serializers.PrimaryKeyRelatedField(queryset = Categories.objects.all())
    userId = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = RentItem
        fields = ["id",'title','price','thumbnailImage','description','inStock','created','address','latitude','longitude','itemRules','category','userId','status']

    def get_userId(self,obj):
        return obj.users.id

    def create(self,validated_data):
        category = validated_data.pop('category')
        rent_item = RentItem.objects.create(category = category, **validated_data)
        return rent_item

    def get_itemRules(self,obj):
        rules = [rule.rule_text for rule in obj.rules.all()]
        return list(rules)

class CategorySerializer(serializers.ModelSerializer):
    rent_category = RentItemSerializer(many=True , read_only = True)
    class Meta:
        model = Categories
        fields = ["id","category_name",'rent_category']


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ["rule_text"]


class UserListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserListing
        fields = "__all__"
        

