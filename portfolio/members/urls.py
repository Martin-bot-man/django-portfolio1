from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
]