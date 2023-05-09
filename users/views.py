from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse("Invalid credentials")


    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})