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


import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import UserRegistration  # Assuming the model name is UserRegistration
from django.conf import settings

def generate_otp():
    """Generates a random 6-digit OTP."""
    return random.randint(100000, 999999)

def registration_view(request):
    if request.method == 'POST':
        # Collect user details from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        
        # Generate OTP and store in session
        otp = generate_otp()
        request.session['otp'] = otp
        request.session['user_data'] = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'dob': dob,
            'gender': gender,
        }

        # Send OTP to the user's email
        send_mail(
            'Your OTP for Registration',
            f'Your OTP is {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        # Redirect to OTP verification page
        return redirect('verify_otp')

    return render(request, 'inventory/registration.html')

from django.shortcuts import render, redirect

from django.contrib import messages

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        sent_otp = request.session.get('otp')

        if entered_otp == str(sent_otp):
            # OTP is correct, save user data to the database
            user_data = request.session.get('user_data')
            user = UserRegistration.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                mobile=user_data['mobile'],
                dob=user_data['dob'],
                gender=user_data['gender']
            )
            user.save()

            # Clear the session data
            del request.session['otp']
            del request.session['user_data']

            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('verify_otp')

    return render(request, 'inventory/verify_otp.html')

