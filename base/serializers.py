from rest_framework import serializers
from base.models import Categories,Rules,RentItem,Booking

class RentItemSerializer(serializers.ModelSerializer):
    itemRules = serializers.SerializerMethodField(read_only = True)
    category = serializers.PrimaryKeyRelatedField(queryset = Categories.objects.all())
    owner = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = RentItem
        fields = ["id",'title','price','thumbnailImage','description','inStock','created','address','latitude','longitude','itemRules','category','owner','status']

    def get_owner(self,obj):
        return obj.owner.id

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


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    user_id = serializers.SerializerMethodField(read_only = True)
    title = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Booking
        fields = ['id','user_id','rent_item','title','start_date','end_date','total_price','status']
    
    def get_user_id(self,obj):
        return obj.user.id
    
    def get_title(self,obj):
        return obj.rent_item.title

    def validate(self, data):
        # ensure end date is after start date
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date")
        
        # check if the item is available during the selected dates 
        overlapping_bookings = Booking.objects.filter(rent_item = data['rent_item'], start_date__lt=data['end_date'],end_date__gt=data['start_date'])
        if overlapping_bookings.exists():
            raise serializers.ValidationError("This item is already booked for the selected date.")
        return data
    

class UpdateBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']
        extra_kwargs = {
            'status':{
                'required': True
            }
        }

    def validate_status(self,value):
        if value not in [choice[0] for choice in Booking.Status.choices]:
            raise serializers.ValidationError("Invalid status value")
        return value