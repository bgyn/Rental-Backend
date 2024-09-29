from rest_framework import serializers
from base.models import Categories,Rules,RentItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id","category_name",]


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ["rule_text"]

class RentItemSerializer(serializers.ModelSerializer):
    itemRules = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = RentItem
        fields = ["id",'title','price','thumbnailImage','description','quantity','created_at','rating','numOfReviews','address','latitude','longitude','itemRules',]

    def get_itemRules(self,obj):
        rules = [rule.rule_text for rule in obj.rules.all()]
        return list(rules)