from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('new/', views.create_post, name='create_post'),
]
