from rest_framework import serializers
from base.models import Categories,RentItem,Booking

class RentItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset = Categories.objects.all())
    owner = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = RentItem
        fields = ["id",'title','price','thumbnailImage','description','inStock','created','address','latitude','longitude','rules','category','owner','status']

    def get_owner(self,obj):
        return obj.owner.id

    def create(self,validated_data):
        category = validated_data.pop('category')
        rent_item = RentItem.objects.create(category = category, **validated_data)
        return rent_item

class UpdateRentItemSerializer(serializers.ModelSerializer):
    thumbnailImage = serializers.ImageField(required=False)
    class Meta:
        model = RentItem
        fields = ['title','price','thumbnailImage','description','inStock','address','latitude','longitude','rules','category']

class CategorySerializer(serializers.ModelSerializer):
    rent_category = RentItemSerializer(many=True , read_only = True)
    class Meta:
        model = Categories
        fields = ["id","category_name",'rent_category']



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