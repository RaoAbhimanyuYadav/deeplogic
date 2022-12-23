from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


def homepage(request):
    message = 'Please Login to visit website'
    isLogin = False
    if request.user.is_authenticated:
        message = 'Now you can upload and view uploaded files'
        isLogin = True
    context = {'message': message, 'isLogin': isLogin}
    return render(request, 'user/homepage.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # This will create a session token and write it in cookies
                # and also add it to django_session database
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or Password is incorrect')
        except:
            messages.error(request, 'Username not found.')
    return render(request, 'user/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged out.')
    return redirect('login')


def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'User account was created')
                login(request, user)
                return redirect('index')
            except:
                messages.error(request, "User already exists")
        else:
            messages.error(request, "Some error occurred while creating the user")
    context = {'page': 'register', 'form': form}
    return render(request, 'user/login_register.html', context)
