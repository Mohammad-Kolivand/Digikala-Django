from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import CustomerProfile, SellerProfile


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password.",
                "username": username,
            },
        )

    return render(request, "accounts/login.html")


def signup_view(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        phone = request.POST.get("phone", "").strip()
        role = request.POST.get("role")

        if form.is_valid():

            if role not in {"customer", "seller"}:
                form.add_error(
                    None,
                    "Please select a valid account type."
                )

            else:
                user = form.save()

                if role == "customer":
                    CustomerProfile.objects.create(
                        user=user,
                        phone=phone
                    )
                else:
                    SellerProfile.objects.create(
                        user=user,
                        phone=phone
                    )

                return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/signup.html",
        {"form": form},
    )