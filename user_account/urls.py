from django.urls import path
from user_account import views

urlpatterns = [
    path('',views.account),
    path('signup/',views.signup, name="signup"),
]