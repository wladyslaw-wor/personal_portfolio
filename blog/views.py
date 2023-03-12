from django.shortcuts import render, get_object_or_404
from .models import Blog
from portfolio.models import Link, Identic

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    links = Link.objects.all()
    identics = Identic.objects.first()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'links':links, 'identic':identics})

def detail(request, blog_id):
    links = Link.objects.all()
    blog = get_object_or_404(Blog, pk=blog_id)
    identics = Identic.objects.first()
    return render(request, 'blog/detail.html', {'blog':blog, 'links':links, 'identic':identics})