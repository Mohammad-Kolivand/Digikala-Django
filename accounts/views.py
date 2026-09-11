from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


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
                "error": "نام کاربری یا رمز عبور اشتباه است.",
                "username": username,
            },
        )

    return render(request, "accounts/login.html")