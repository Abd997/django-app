from django.contrib import admin
from django.urls import path, include
from crudApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("crudApp.urls")),
]
