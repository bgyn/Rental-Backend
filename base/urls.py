from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoryView.as_view(),name="categories"),
    path('rules/',views.RuleView.as_view(),name="rule"),
    path('rentlist/',views.RentItemView.as_view(),name = "rentItem"),
    path('rentlist/<int:pk>/',views.RentItemDetailView.as_view(),name="rentItemDetail"),
    path('my_listing/',views.UserListingView.as_view(), name='my-listing'),
    path('booking/',views.BookingView.as_view(),name='booking'),
]