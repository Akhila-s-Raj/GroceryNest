from django.urls import path
from .views import grocery_index, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', grocery_index, name='grocery_index'),  # Home page
    path('login/', login_view, name='login'),        # Login page
   
]
