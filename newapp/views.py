from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request, "home.html", {'blog_posts':blog})

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    if request.FILES:
        blog.image = request.FILES['post_image']
    blog.save()

    return redirect('home')

def read(request, post_id):
    blog = get_object_or_404(Blog, pk=post_id)
    return render(request, 'read.html', {'blog':blog})

    #{'':} '' 안에 들어가는 것이 html에서 출력되는 것임.

def update(request, post_id):
    updated_post = get_object_or_404(Blog, pk=post_id)
    updated_post.title = request.POST['title']
    updated_post.body = request.POST['body']
    updated_post.save()
    return redirect('/read/' + str(updated_post.id)) #수정을 하는 함수. 

def renew(request, post_id): #update 페이지랑 연결
    renew_post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'renew.html', {'renew' : renew_post})

def delete(request, blog_id):
    deleted_post = get_object_or_404(Blog, pk=blog_id)
    deleted_post.delete()
    return redirect('home')

    
