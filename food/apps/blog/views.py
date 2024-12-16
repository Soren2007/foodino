# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
# from django.views.generic.edit import DeleteView
from django.http import Http404
from django.contrib.messages import success,error
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def add_key_word(request):
    if request.method == 'POST':
        key_word = KeyWord()
        key_word.word = request.POST['word']
        key_word.save()
    return render(request, 'blog/key_word/add.html')
def delete_key_word(request,id):
    KeyWord.object.get(id=id).delete()
    return render(request, 'blog/key_word/show_key_words.html')
def edit_key_word(request,id):
    return render(request, 'blog/key_word/edit.html')
def show_key_word(request,id):
    return render(request, '',{"key_word":KeyWord.object.get(id=id)})
def show_key_words(request):
    return render(request, 'blog/key_word/show_key_words.html',{"key_words":KeyWord.object.all()})

def add_article(request):
    if request.method == 'POST':
        article = Article()
        article.article_title = request.POST.get('article_title')
        article.article_slug = request.POST.get('article_slug')
        article.article_main_image = request.POST.get('article_main_image')
        article.article_summary_text = request.POST.get('article_summary_text')
        article.article_main_text = request.POST.get('article_main_text')
        article.article_key_words = request.POST.get('article_key_words')
        article.article_visits = request.POST.get('article_visits')
        article.article_group = request.POST.get('article_group')
        article.article_author = request.POST.get('article_author')
        if request.POST.get('article_is_active') == "on":article.article_is_active = True
        else:article.article_is_active = False
        article.save()
        return render(request, 'blog/article/show_authors.html')
    else:
        return render(request, 'blog/article/add.html')
        # 633312463 پادا
def delete_article(request,id):
    Article.objects.get(id=id).delete()
    return render(request, 'blog/article/delete.html')
def edit_article(request,slug):
    return render(request, 'blog/article/edit.html')
def show_article(request,slug):
    try:
        article = Article.objects.get(article_slug=slug)
    except ObjectDoesNotExist:
        error(request,_("مقاله پیدا نشد!"))
        return redirect("main_app:index")
    article.article_short_url = f"{settings.URL}blog/{article.id}"
    article.article_visits = article.article_visits + 1
    article.save()
    return render(request, 'blog/article/show.html',{"article":article,'slug':slug,'model':'blog'})

def show_article_with_id(request,id):
    article = Article.objects.get(id=id)
    article.article_visits = article.article_visits + 1
    article.save()
    return render(request, 'blog/article/show.html',{"article":article,'slug':article.article_slug,'model':'blog'})
def show_article_with_author(request,author_slug):
    try:
        author=Author.objects.get(slug=author_slug)
    except:
        error(request,"","error")
        return redirect("blog_app:show_blogs")
    articles=Article.objects.filter(article_slug=author)
    page_object_number = 12
    paginator=Paginator(articles,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/article/show_articles.html',{"page_obj":page_obj,'obj_len':len(articles),'page_object_number':page_object_number})

# def show_all_article_with_(request):
#     articles=Article.objects.all()
def show_all_article(request):
    articles=Article.objects.all()
    page_object_number = 12
    paginator=Paginator(articles,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/article/show_articles.html',{"page_obj":page_obj,'obj_len':len(articles),'page_object_number':page_object_number})
def add_author(request):
    if request.method == 'POST':
        author = Author()
        author.author_avatar = request.POST.get('author_avatar')
        author.author_name = request.POST.get('author_name')
        author.author_family = request.POST.get('author_family')
        author.author_email = request.POST.get('author_email')
        author.author_phone = request.POST.get('author_phone')
        author.author_info = request.POST.get('author_info')
        author.author_slug = request.POST.get('author_slug')
        if request.POST.get('author_is_active') == "on":author.author_is_active = True
        else:author.author_is_active = False
        author.save()
        return render(request, 'blog/author/show_authors.html')
    else:
        return render(request, 'blog/author/add.html')

def delete_author(request,id):
    Author.objects.get(id=id).delete()
    return render(request, 'blog/author/delete.html')
def edit_author(request,id):
    return render(request, 'blog/author/edit.html')
def show_author(request,slug):
    try:
        author= Author.objects.get(author_slug=slug)
    except Author.DoesNotExist:
        raise Http404("صفحه مورد نظر شما یافت نشد")
    return render(request, 'blog/author/show.html',{"author":author})
def show_all_author(request):
    authors=Author.objects.filter(is_active = True)
    paginator=Paginator(authors,1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/author/show_authors.html',{"page_obj":page_obj})



def add_like(request):
    blog_id = request.GET.get("blog_id")
    try:
        blog = Article.objects.get(id=blog_id)
        blog.article_likes = blog.article_likes+1
        blog.save()
        return HttpResponse(blog.article_likes)
    except ObjectDoesNotExist:
        return HttpResponse('مقاله پیدا نشد.')
    except:
        return HttpResponse(_("خطا در اجرای عملیات!"))

def add_dislike(request):
    blog_id = request.GET.get("blog_id")
    try:
        blog = Article.objects.get(id=blog_id)
        blog.article_dislikes = blog.article_dislikes+1
        blog.save()
        return HttpResponse(blog.article_dislikes)
    except ObjectDoesNotExist:
        return HttpResponse('مقاله پیدا نشد.')
    except:
        return HttpResponse(_("خطا در اجرای عملیات!"))