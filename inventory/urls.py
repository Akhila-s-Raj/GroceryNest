from django.urls import path
#from .views import grocery_index, login_view, views.registration_view,views.verify_otp
from . import views  # Import the views module
from .views import grocery_index, login_view, registration_view, verify_otp
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', grocery_index, name='grocery_index'),  # Home page
    path('login/', login_view, name='login'),        # Login page
    path('register/', views.registration_view, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
   
]
