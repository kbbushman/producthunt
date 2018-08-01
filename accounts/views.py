from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib import auth

############################ SIGN UP ############################

def signup(request):
  # POST Request for a new user
  if request.method == 'POST':
    # Verify passwords
    if request.POST['password1'] == request.POST['password2']:
      try:
        # If Username already exists, render form with error
        user = User.objects.get(username=request.POST['username'])
        return render(request, 'accounts/signup.html', {'error': 'Username already in use'})
      # If user does not exist, create and login new user then redirect to home
      except User.DoesNotExist:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        profile = Profile.objects.create(user=user)
        auth.login(request, user)
        return redirect('home')
    else:
      return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
  # GET request for empty sign up form
  else:
    return render(request, 'accounts/signup.html')

############################ LOGIN ############################

def login(request):
  if request.method == 'POST':
    # Verify username exists and passwords match
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    # If authenticate returns a user
    if user is not None:
      # Log the user in and redirect home
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
  # GET request for blank login form
  else:
    return render(request, 'accounts/login.html')

############################ LOGOUT ############################

def logout(request):
  # if request.method == 'POST':
  auth.logout(request)
  return redirect('home')
