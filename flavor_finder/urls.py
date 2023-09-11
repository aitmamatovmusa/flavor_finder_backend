from django.contrib import admin
from django.urls import path, include
from accounts.views import Register, Login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("register/", Register.as_view()),
    path("login/", Login.as_view())
]
