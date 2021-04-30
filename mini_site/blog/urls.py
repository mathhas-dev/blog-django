from django.urls import path, include
from blog.views import post_list, post_detail, post_new

urlpatterns = [
    path('blog/', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
]