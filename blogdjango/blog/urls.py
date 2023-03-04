from .views import *
from django.urls import path

urlpatterns = [
    path('', show_news, name='show_news'),
    path('new_detail/<int:pk>/', new_detail, name='new_detail'),
    path('create_news/', create_news, name='create_news'),
    path('update_news/<int:pk>', update_news, name='update_news'),
    path('delete_news/<int:pk>', delete_news, name='delete_news'),
    path('show_category/<int:pk>', show_category, name='show_category'),
]

