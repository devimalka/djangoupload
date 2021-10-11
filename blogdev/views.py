from typing import List
from django import http
from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

import blogdev
from . models import Post
from django.template import loader
from django.core.paginator import Paginator
from taggit.models import Tag
from django.views.generic import ListView
from django.db.models import Q



# Create your views here.
def index(request):
    posts = Post.objects.all()
    pages = Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)
    context = {
        'posts':page_obj
    }
    return render(request,'blogdev/post.html',context)
   
    

def post(request,id):
   post = get_object_or_404(Post,pk=id)
   return render(request,'blogdev/detail.html',{'post':post})


# def tagged(request,tag__slug=None):
#     if tag__slug:
#         tag = get_object_or_404(Tag,slug=tag__slug)
#         posts = Post.objects.all()
#         posts = posts.filter(tagged_items=[tag])
#         context = {
#             'tag':tag,
#             'posts':posts,
#         }
#         return render(request,'blogdev/tagview.html',context)


class tagListView(ListView):
    template_name = 'blogdev/tagview.html'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):
        context = super(tagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context


def search(request):
    if request.method == 'POST':
        searched = request.POST['query']
        if searched:
            # posts = Post.objects.all()
            results = Post.objects.filter(title__contains=searched)
            context ={
                'posts':results
            }
            return render(request,'blogdev/results.html',context)
        else:
            return render(request,'blogdev/results.html')
    
        
