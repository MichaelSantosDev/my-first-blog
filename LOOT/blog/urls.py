from django.urls import path
from .views import post_list
from .views import post_detail
from .views import post_new




urlpatterns = [
    path('post_list/', post_list, name="post_list"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
]