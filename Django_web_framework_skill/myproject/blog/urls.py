from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', views.update_post, name='update_post'),


    path('new/', views.create_post, name='create_post'),
]
