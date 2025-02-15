from django.shortcuts import redirect
from django.conf import settings

class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == "/home":
            return redirect("login")
        elif request.user.is_authenticated and request.path == "/":
            return redirect("home")
        return self.get_response(request)
