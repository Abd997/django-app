from django.urls import path
from crudApp import views

urlpatterns = [
    path("", views.index, name="crudApp"),
    path("signin/", views.sign_in, name="crudApp"),
    path("signup/", views.sign_up, name="crudApp"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
