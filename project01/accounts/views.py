from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


# Create your views here.
def register_page(request):
    if request.user.is_authenticated:
        return redirect('todos:homepage')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +  user)
                return redirect('login_page')
        args = {'form': form}
        return render(request, 'register.html', args)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('todos:homepage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('todos:homepage')
                # Redirecting to a different app does not work
                #return HttpResponseRedirect('todos: homepage')
            else:
                messages.info(request, 'Username OR password is incorrect')
        args = {}
        return render(request, 'login.html', args)

def logout_user(request):
    logout(request)
    return redirect('login_page')