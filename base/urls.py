from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('categories/',views.CategoryView.as_view(),name="categories"),
    path('rules/',views.RuleView.as_view(),name="rule"),
    path('rentItem/',views.RentItemView.as_view(),name = "rentItem"),
    path('rentItem/<int:pk>/',views.RentItemDetailView.as_view(),name="rentItemDetail"),
]