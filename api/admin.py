from django.contrib import admin
from api.models import Category,RentList,Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(RentList)
