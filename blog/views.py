from django.shortcuts import render
from .models import BlogModel,Category,Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def blogview(request):
    categories=Category.objects.all()
    posts=BlogModel.objects.order_by('-created_at').filter(is_apporved=True)
    news = BlogModel.objects.filter(title__iexact='build a wEATher website – Django project for beginners')
    context={
        'posts':posts,
        'categories':categories,
        'news':news
    }
    return render(request,'blog/posts.html',context)

def single_view(request,slug):
    post = BlogModel.objects.get(slug=slug)
    comments = post.comments.all().filter(is_apporved=True)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        data=Comment(post=post,name=name,email=email,comment=comment)
        data.save()
    context={
        'post':post,
        'comments':comments,
        }
    return render(request,'blog/post.html',context)

def category_view(request,name):
    category=Category.objects.get(name=name)
    posts =BlogModel.objects.all().filter(category=category)
    context={

        'posts':posts,
        'name':name
    }
    return render(request,'blog/category.html',context)


def search(request):
    if request.method == 'POST':
        search_item = request.POST['search']
        posts = BlogModel.objects.filter(Q(title__icontains = search_item)|Q(descriptipon__icontains = search_item))
        context={

            'posts':posts,
            'search_item':search_item
        }
    return render(request,'blog/search.html',context)




            