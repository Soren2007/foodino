# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from apps.food.models import Food,Recipes,StuffGroup,Stuff,FoodGroup,FoodStuffType,Meal,MyRecipes
from apps.accounts.models import Country,City,CustomUser,Customer
from apps.blog.models import KeyWord,Author,Article
from apps.branch.models import Branch
from apps.comments.models import Comment
from apps.discounts.models import Coupon,DiscountBasket,DiscountBasketDetail
from apps.favorites.models import Favorite
from apps.message.models import Message,UserChatRoom,ChatRoom
from apps.mukbang.models import Mukbang
from django.conf import settings
from utils import Scrap,image_saver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import error,success
from .models import Slid,frequently_asked_question
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# import subprocess
from platform import uname
# Create your views here.

app_name = "main_app"

def template_data(request):
    return {"media":settings.MEDIA_URL,"base_url":settings.URL}
def objects(request):
    foods_length = len(Food.objects.all())
    latest_food_sales_number = Food.objects.all().order_by('-food_sales_number')[:8]
    latest_recipes = Recipes.objects.all().order_by('-recipe_register_date')[:8]
    latest_articles = Article.objects.all().order_by('-article_register_date')[:8]
    return {"latest_food_sales_number":latest_food_sales_number,"latest_recipes":latest_recipes,"latest_articles":latest_articles,"foods_length":foods_length}

@ensure_csrf_cookie
def index(request):
    slides = Slid.objects.filter(Q(slid_is_active = True) & Q(slid_start_date_time__lt = timezone.now()) & Q(slid_end_date_time__gt = timezone.now()))
    mukbangs = Mukbang.objects.filter(is_active=True)[:4:-1]
    return render(request,'main/index.html',{'slides':slides,'mukbangs':mukbangs,})

def about_me(request):
    return render(request,'main/about_me.html')
def rules(request):
    return render(request,'main/rules.html')

def http_status_404(request,exception):
    print(exception)
    return redirect("main_app:index")

from re import findall
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from os.path import exists
from django.http import FileResponse
def download(request,file_path,content_type="application/pdf"):
    file_path = f"{settings.BASE_DIR}{file_path}"
    file_path  = findall(r'media\\(.*)',file_path)[0]
    if content_type == "image":
        content_type = "application/image/png"
    elif content_type == "pdf":
        content_type = "application/pdf"
    print(content_type)
    file_system_storage = FileSystemStorage() 
    if file_system_storage.exists(file_path):
        with file_system_storage.open(file_path,"rb") as file:
            # content_type="image/jpeg"
            return HttpResponse(file,content_type="image/jpg")
            
    error(request,_("فایل پیدا نشد."),"error")
    return redirect("main_app:index")
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from os.path import splitext
def save_image(request):
    if request.method == 'POST':
        imageUpload = request.FILES['image']
        title = request.POST.get("title")
        if imageUpload.size > 1000: #byt
            image_name,image_ext = splitext(imageUpload.name)
            current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            # image_path = "images/main/"+ image_name+current_time+image_ext
            image_path = "images/main/"+ title
            fss=FileSystemStorage()
            fss.save(image_path,imageUpload)
            redirect("main_app:index")
    else:
        return render(request, 'main/upload_image.html')
    
def show_frequently_asked_questions(request):
    frequently_asked_questions = frequently_asked_question.objects.filter(is_active = True).order_by('-register_date')
    return render(request, "main/frequently_asked_questions.html", {"frequently_asked_questions":frequently_asked_questions})
    