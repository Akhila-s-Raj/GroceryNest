from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def grocery_index(request):
    return render(request, 'inventory/grocery_index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('grocery_index')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

from django.shortcuts import render

def profile_view(request):
    return render(request, 'inventory/profile.html')  # Create a template named profile.html
