from django.urls import path
from api import views

urlpatterns = [
    path('',views.index),
    path('categories/', views.CategoryView.as_view(), name= "category"),
    path('rentlist/',views.RentListView.as_view(), name="rentlist"),
]