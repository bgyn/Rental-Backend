from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoryView.as_view(),name="categories"),
    path('rules/',views.RuleView.as_view(),name="rule"),
    path('rentitem/',views.RentItemView.as_view(),name = "rentItem"),
    path('rentitem/<int:pk>/',views.RentItemDetailView.as_view(),name="rentItemDetail"),
]