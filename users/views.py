from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        # View to render form
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                # User is authenticated
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')


    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'users/index.html')