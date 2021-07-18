'''
n url.py, the most important thing is the "urlpatterns" tuple.
It's where you define the mapping between URLs and views.
A mapping is a tuple in URL patterns like − from django. conf. urls import patterns,
include, url from django.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createBlog/', views.create_blog, name='createBlog'),
    path('searchBlog/', views.search_blog, name='searchBlog'),
    path('updateBlog/<int:_pk>/', views.update_blog, name='updateBlog'),
    path('deleteBlog/<int:_pk>/', views.delete_blog, name='deleteBlog'),
]
