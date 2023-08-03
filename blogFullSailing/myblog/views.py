from django.shortcuts import render, get_object_or_404
from .models import Page, Blog

# Create your views here.

def about(request):
    return render(request, 'myblog/about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'myblog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id)
    return render(request, 'myblog/blog_detail.html', {'blog': blog})

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'myblog/page_list.html', {'pages': pages})