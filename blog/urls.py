from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createBlog/', views.createBlog, name='createBlog'),
    path('searchBlog/', views.searchBlog, name='searchBlog'),
    path('updateBlog/<int:pk>/', views.updateBlog, name='updateBlog'),
    path('deleteBlog/<int:pk>/', views.deleteBlog, name='deleteBlog'),
]
