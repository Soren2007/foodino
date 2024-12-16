# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.messages import success,error
from .models import *
from .forms import *
from apps.food.models import Food
from apps.blog.models import Article
from apps.accounts.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

class CommentView(View):
    def get(self,request,*args,**kwargs):
        food_id = request.GET.get('food_id')
        comment_id = request.GET.get('comment_id')
        slug = kwargs['slug']
        model = kwargs['model']
        initial_dict = {
            'food_id':food_id,
            'comment_id':comment_id,
        }
        form = CommentForm(initial=initial_dict)
        return render(request,'comments/partials/create_comment.html',{'form':form,'slug':slug,'model':model})
    def post(self,request,*args,**kwargs):
        model = kwargs.get('model')
        slug = kwargs.get('slug')
        form = CommentForm(request.POST)
        if form.is_valid():
            if model == 'food':
                food = get_object_or_404(Food,food_slug=slug)
                data = form.cleaned_data
                parent = None
                if data['comment_id']:
                    parent_id=data['comment_id']
                    try:
                        parent = Comment.objects.get(id=parent_id)
                    except ObjectDoesNotExist:
                        error(request,_('نظر پیدا نشد.'),'error')
                        redirect('food_app:show_food',food.food_slug)
                    except:
                        error(request,_('خطا در انجام عملیات!'),'error')
                        redirect('food_app:show_food',food.food_slug)
                if request.user.is_support:
                    comment = Comment.objects.create(food=food,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent,is_active = True)
                else:
                    comment = Comment.objects.create(food=food,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent)
                    success(request,_('نظر شما با موفقیت ثبت شد. بعد از تایید پشتیبانان نظر شما به نمایش در می‌آید. سپاس از شما🙏🏻'),'success')
                    return redirect('food_app:show_food',food.food_slug)
                return redirect('food_app:show_food',food.food_slug)            
            elif model == 'blog':
                blog = get_object_or_404(Article,article_slug=slug)
                data = form.cleaned_data
                parent = None
                if data['comment_id']:
                    parent_id=data['comment_id']
                    try:
                        parent = Comment.objects.get(id=parent_id)
                    except ObjectDoesNotExist:
                        error(request,_('نظر پیدا نشد.'),'error')
                        redirect('blog_app:show_blog',blog.article_slug)
                    except:
                        error(request,_('خطا در انجام عملیات!'),'error')
                        redirect('blog_app:show_blog',blog.article_slug)
                if request.user.is_support:
                    comment = Comment.objects.create(blog=blog,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent,is_active = True)
                else:
                    comment = Comment.objects.create(blog=blog,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent)
                    success(request,_('نظر شما با موفقیت ثبت شد. بعد از تایید پشتیبانان نظر شما به نمایش در می‌آید. سپاس از شما🙏🏻'),'success')
                    return redirect('blog_app:show_blog',blog.article_slug)
                return redirect('blog_app:show_blog',blog.article_slug)
            elif model == 'recipe':
                recipe = get_object_or_404(Recipes,recipe_slug=slug)
                data = form.cleaned_data
                parent = None
                if data['comment_id']:
                    parent_id=data['comment_id']
                    try:
                        parent = Comment.objects.get(id=parent_id)
                    except ObjectDoesNotExist:
                        error(request,_('نظر پیدا نشد.'),'error')
                        redirect('food_app:show_recipe',recipe.recipe_slug)
                    except:
                        error(request,_('خطا در انجام عملیات!'),'error')
                        redirect('food_app:show_recipe',recipe.recipe_slug)
                if request.user.is_support:
                    comment = Comment.objects.create(recipes=recipe,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent,is_active = True)
                else:
                    comment = Comment.objects.create(recipes=recipe,commenting_user=request.user,comment_text=data['comment_text'],comment_parent = parent)
                    success(request,_('نظر شما با موفقیت ثبت شد. بعد از تایید پشتیبانان نظر شما به نمایش در می‌آید. سپاس از شما🙏🏻'),'success')
                    return redirect('food_app:show_recipe',recipe.recipe_slug)
                
                return redirect('food_app:show_recipe',recipe.recipe_slug)
            else:
                error(request,_('خطا در انجام عملیات!'),'error')
                return redirect('main_app:index')
def show_my_comments(request):
    from django.core.paginator import Paginator
    user = request.user
    comments = Comment.objects.filter(commenting_user=CustomUser.objects.get(id=user.id))
    page_object_number = 12
    paginator=Paginator(comments,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'comments/show_my_comments.html',{"page_obj":page_obj,'obj_len':len(comments),'page_object_number':page_object_number})