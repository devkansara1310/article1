from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from  .forms import articalForm
from .models import Artical,Tag
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from itertools import chain
from django.db.models import Count
# Create your views here.

def post(request):
    user=request.user.id
    tags_objs=[]
 
    if request.method == 'POST':
        title=request.POST.get("title")
        content=request.POST.get("content")
        status=request.POST.get("status")
        tags_form=request.POST.get("tags")
        print(request.user)
        print(title)
        print(content)
        print(status)
        print(tags_form)
            
        title=request.POST.get("title")
        content=request.POST.get("content")
        status=request.POST.get("status")
        tags_form=request.POST.get("tags")
        user=request.user
        tags_list=list(tags_form.split(","))

        for tag in tags_list:
            t,created = Tag.objects.get_or_create(name=tag)
            tags_objs.append(t)
        
        p, created = Artical.objects.get_or_create(title=title,User=user,content=content,status=status)
        p.tags.set(tags_objs)
        p.save
        return redirect('index')

    return render(request,'post.html')    

def tags(request, slug):
    artical = Artical.objects.filter('published')
    queryset = Artical.objects.all()
    queryset2 = queryset.annotate(num_times=Count('taggit_taggeditem_items'))
    context = {

    }
    return render(request,'view.html',context)

def feed(request): 
    artical=Artical.objects.filter(status="publish")
    # xx=Artical.objects.values_list('tags')
    # print(xx)
    
    context={
        'artical':artical,
    }
    return render(request,'compose.html',context)    


def index(request):
    obj=Artical.objects.all()
    tags = Tag.objects.values('name').annotate(total=Count('name'))
    context ={
        "obj":obj,    
        'tags':tags,
    }
    return render(request,'index.html',context)

def tag(request,slug):
    
    obj = Artical.objects.filter(tags__name__contains=slug)
    tags = Tag.objects.values('name').annotate(total=Count('name'))
    context = {
        'obj':obj,
        'tags':tags,
    }
    return render(request,"tags.html",context)


# def like(request):
#     artical = get_object_or_404(Artical, id=request.POST.get('article_id'))
#     artical.likes.add(request.user.id)
#     return HttpResponseRedirect(reverse('show', args=[str(pk)]))
