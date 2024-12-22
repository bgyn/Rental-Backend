from django.contrib import admin
from base.models import Categories,Rules,RentItem,Booking

# Register your models here.
admin.site.register(Categories)
admin.site.register(Rules)

@admin.register(RentItem)
class RentItemAdmin(admin.ModelAdmin):
    list_display = ['owner','title','price','inStock','status']
    list_filter = ['created','status']
    list_editable = ['status']
    search_fields = ['title']

admin.site.register(Booking)