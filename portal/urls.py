from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    #Here, create a path to call the view.py by importing views. Then Goto views to create the function to be rendered.
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]