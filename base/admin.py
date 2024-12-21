from django.contrib import admin
from base.models import Categories,Rules,RentItem

# Register your models here.
admin.site.register(Categories)
admin.site.register(Rules)

@admin.register(RentItem)
class RentItemAdmin(admin.ModelAdmin):
    list_display = ['users','title','price','rating','inStock','rating','numOfReviews','status']
    list_filter = ['created','status']
    list_editable = ['status']
    search_fields = ['title']