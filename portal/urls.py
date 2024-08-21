from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    #Here, create a path to call the view.py by importing views. Then Goto views to create the function to be rendered.
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('modify_record/<int:pk>', views.modify_record, name='modify_record'),
]