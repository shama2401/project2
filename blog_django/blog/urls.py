from .views import *
from django.urls import path

urlpatterns = [
    path('', show_news, name='show_news'),
    path('new_detail/<int:pk>/', new_detail, name='new_detail'),
]
