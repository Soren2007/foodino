# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from apps.food.models import Food
from apps.blog.models import Article
from .models import *
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.contrib.messages import error,success
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def add_to_favorite(request):
    if request.method == "POST":
        food_id = request.POST.get('food_id')
        try:
            food=Food.objects.get(id=food_id)
        except:
            error(request, "همچین غذایی وجود ندارد!","error")
            redirect('favorit_app')
        flag = Favorite.objects.filter(Q(favorite_user_id=request.user.id) & Q(food_id=food_id)).exists()
        if not flag:
            Favorite.objects.create(food=food, favorite_user=request.user)
            return HttpResponse(_('این غذا به لیست علایق شما اضافه شد.'))
        return HttpResponse(_('این غذا قبلا در لیست غلایق شما قرار گرفته است.'))

def delete_to_favorite(request):
    if request.method == "POST":
        food_id = request.POST.get('food_id')
        try:
            food=Food.objects.get(id=food_id)
        except:
            error(request, "همچین غذایی وجود ندارد!","error")
            redirect('favorites_app:user_favorite')
        flag = Favorite.objects.filter(Q(favorite_user_id=request.user.id) & Q(food_id=food_id)).exists()
        if flag:
            Favorite.objects.filter(food=food, favorite_user=request.user)[0].delete()
            return HttpResponse(_('این غذا از لیست علایق شما حذف شد.'))
        return HttpResponse(_('این غذا قبلا در لیست غلایق شما وجود نداشت.'))

def status_of_favorite(request):
    print(100*'-')
    print(request.method)
    print(100*'-')
    if request.method == "POST":
        return HttpResponse(len(Favorite.objects.filter(Q(favorite_user_id=request.user.id))) + len(Favorite_Blog.objects.filter(Q(favorite_user_id=request.user.id))))

def add_to_favorite_blog(request):
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        try:
            blog=Article.objects.get(id=blog_id)
        except:
            error(request, _("همچین غذایی وجود ندارد!"),"error")
            redirect('favorit_app:user_favorite')
        flag = Favorite_Blog.objects.filter(Q(favorite_user_id=request.user.id) & Q(blog_id=blog_id)).exists()
        if not flag:
            Favorite_Blog.objects.create(blog=blog, favorite_user=request.user)
            return HttpResponse(_('این مقاله به لیست علایق شما اضافه شد.'))
        return HttpResponse(_('این مقاله قبلا در لیست غلایق شما قرار گرفته است.'))
    

def delete_to_favorite_blog(request):
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        try:
            blog=Article.objects.get(id=blog_id)
        except:
            error(request, _("همچین مقاله‌ای وجود ندارد!"),"error")
            redirect('favorites_app:user_favorite')
        flag = Favorite_Blog.objects.filter(Q(favorite_user_id=request.user.id) & Q(blog_id=blog_id)).exists()
        if flag:
            Favorite_Blog.objects.filter(blog=blog, favorite_user=request.user)[0].delete()
            return HttpResponse(_('این مقاله از لیست علایق شما حذف شد.'))
        return HttpResponse(_('این مقاله قبلا در لیست غلایق شما وجود نداشت.'))


class UserFavoriteView(View):
    def get(self, request, *args, **kwargs):
        favorite_food_user = Favorite.objects.filter(Q(favorite_user_id=request.user.id))
        favorite_blog_user = Favorite_Blog.objects.filter(Q(favorite_user_id=request.user.id))
        return render(request, 'favorites/user_favorite.html',{'favorite_food_user':favorite_food_user,'favorite_blog_user':favorite_blog_user})