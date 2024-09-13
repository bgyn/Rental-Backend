from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('categories/',views.CategoryView.as_view(),name="categories"),
]