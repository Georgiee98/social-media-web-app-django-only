from django.shortcuts import render

from .forms import LoginForm

# View to render form
def user_login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})