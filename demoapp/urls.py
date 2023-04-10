from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adduser', views.adduser, name="adduser"),
    path('viewusers', views.viewusers, name="viewusers"),
    path('delete_user', views.delete_user, name="delete_user"),
]
