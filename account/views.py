from django.shortcuts import render
from datetime import date, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from loguru import logger

from account.forms import LoginForm

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            remember_me = cd["remember_me"]

            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)

                    return redirect("user_dashboard")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
