from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("kuw.urls")),
    path('admin/', admin.site.urls),
]
