from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('pages/', views.page_list, name='page_list'),
    path('pages/<int:page_id>', views.page_detail, name='page_detail'),
    path('blogs/<int:blog_id>', views.blog_detail, name='blog_detail'),


]