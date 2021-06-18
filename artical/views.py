from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from.forms import articalForm,tagForm
from .models import Artical,ArticalTag,Tag
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from itertools import chain
from django.db.models import Count
# Create your views here.

def post(request):
    user=request.user.id
    tags_objs=[]

    form = articalForm() 
    if request.method == 'POST':
        if 'submit' in request.POST:  
            form = articalForm(request.POST)       
            if form.is_valid():
                title=request.POST.get("title")
                content=request.POST.get("content")
                status=request.POST.get("status")
                tags_form=request.POST.get("artical_tag")
                tags_list=list(tags_form.split(","))

                for tag in tags_list:
                    t,created = Tag.objects.get_or_create(name=tag)
                    tags_objs.append(t)

                p, created = ArticalTag.objects.get_or_create(title=title,User=user,content=content,status=status)
                p.tags.set(tags_objs)
                p.save
                return redirect('index')
            else: 
                form = articalForm()

    context={
        'form':form
    }    

    return render(request,'post.html',context)    
    #             article_id=form.save() 
    #             split_tags=article_tags.split(",")
    #             for tag in split_tags:
    #                 obj = ArticalTag.objects.create(name=tag,artical=article_id)
    #                 obj.save()
    #             return redirect('index')
    #         else:
    #             return redirect('post')
    #     elif 'draft' in request.POST:
    #         form = articalForm(request.POST,initial={'status': "draft"})
    #         if form.is_valid():
    #             article_id=form.save()
    #             split_tags=article_tags.split(",")
    #             for tag in split_tags:
    #                 obj = ArticalTag.objects.create(name=tag,artical=article_id)
    #                 obj.save() 
    #             return redirect('index')
    # context={
    #     'form':form,
    # }    
    # return render(request,'post.html',context)



    # form = articalForm() 
    # if request.method == 'POST':
    #     article_tags=request.POST.get("artical_tag")
    #     if 'submit' in request.POST:  
    #         form = articalForm(request.POST,initial={'status': "published"})       
    #         if form.is_valid():
    #             article_id=form.save() 
    #             split_tags=article_tags.split(",")
    #             for tag in split_tags:
    #                 obj = ArticalTag.objects.create(name=tag,artical=article_id)
    #                 obj.save()
    #             return redirect('index')
    #         else:
    #             return redirect('post')
    #     elif 'draft' in request.POST:
    #         form = articalForm(request.POST,initial={'status': "draft"})
    #         if form.is_valid():
    #             article_id=form.save()
    #             split_tags=article_tags.split(",")
    #             for tag in split_tags:
    #                 obj = ArticalTag.objects.create(name=tag,artical=article_id)
    #                 obj.save() 
    #             return redirect('index')
    # context={
    #     'form':form,
    # }    
    # return render(request,'post.html',context)


# class Show(ListView):
#     model = Artical
#     template_name="view.html"
#     context_object_name = "artical"
#     artical= Artical.objects.filter(status='publish')

    
    

# class TagView(ListView):
#     model = Artical
#     template_name="view.html"
#     context_object_name = "artical"
#     artical= Artical.objects.filter(status='publish')
    

#     def get_queryset(self):
#         return Artical.objects.filter(tagged_items=self.kwargs.get('tag_slug'))

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
    print(list(obj))
    article_id = Artical.objects.all().values('id')
    article_id_list=[i['id'] for i in article_id]
    
    print(article_id_list)
    l=[]
    for i in article_id_list:
        article_tag=ArticalTag.objects.filter(artical_id=i).values('name','artical_id')
        # print(article_tag)
        l.append([i['name'] for i in article_tag])
    print(l)
    article_last=[]
    for i in article_id_list:
        article_last.extend(Artical.objects.filter(id=i))
        
    
    # for i in range(len(article)):
    # data_for_template.append(
    #     {
    #         'mListObjA':mList.A,
    #         'mListObjB':mList.B,
    #         'uDictObj':uDict[i], # or i+1 for your example uDict
    #     }
    # )
    # article_tag = ArticalTag.objects.all().values('name','artical_id')
    # print(article_tag)
    article_id1 = ArticalTag.objects.filter(id=7).values('artical_id','id','name')
    # print(article_id1)
    # print("xxxxx")
    # x=[item['id'] for item in objx]
    #   (obj)
    # print(x)
    artical_tag = ArticalTag.objects.filter(artical__id=7)
    id = Artical.objects.all().values_list('id', flat=True)
    
    for i in id:
        object = Artical.objects.filter(id=i).values('id')
        objl=[item['id'] for item in object]
        for i in objl:
            artical_tag = ArticalTag.objects.filter(artical__id=i)
            # print(artical_tag)
    # objl=[item['artical'] for item in artical_tag]
    # print(artical_tag)
    # article=Artical.objects.all()
    # obj=ArticalTag.objects.all()
    # objx= ArticalTag.objects.values('artical_id').annotate(total=Count('artical_id'))
    # objl=[item['id'] for item in objx]
    # objy= ArticalTag.objects.values('artical_id').annotate(total=Count('artical_id'))
    # objy=ArticalTag.objects.filter(artical_id__in=[item['artical_id'] for item in objx])
    # list1=([item.artical_id for item in objy])
    # print(list1)
    # x1=[]
    # for i in list1:
    #     if i not in x1:
    #         x1.append(i)
    #     else:
    #         print(i,end=' ')
    # print(objx)
    
    # print(tags)

    # print(article)
    tags = ArticalTag.objects.values('name').annotate(total=Count('name'))
    
    De={'dev':{'tag':'dev'},'de':'as'}
    context ={
        "obj":obj,
        "artical_tag":artical_tag,
        # "article":article,
        'tags':tags,
        'object':object,
        'de':De,
        'article_last':article_last,
    }
    return render(request,'index.html',context)

def tag(request,slug):
    obj=ArticalTag.objects.filter(name=slug)
    tags = ArticalTag.objects.values('name').annotate(total=Count('name'))
    print(obj)
    context = {
        'obj':obj,
        'tags':tags
    }
    return render(request,"tags.html",context)


# def like(request):
#     artical = get_object_or_404(Artical, id=request.POST.get('article_id'))
#     artical.likes.add(request.user.id)
#     return HttpResponseRedirect(reverse('show', args=[str(pk)]))