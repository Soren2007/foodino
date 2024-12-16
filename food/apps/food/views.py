# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect,get_object_or_404
from apps.orders.food_cart import MyRecipeCart
from django.http import HttpResponse
from django.contrib.messages import error,success
from .models import *
from apps.mukbang.models import Mukbang
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
# Food Class
# @login_required
# def add_food(request):
#     if redirect.method == "POST":
#         food = Food()
#         food.food_name = request.POST.get("food_name")
#         food.food_image = request.POST.get("food_image")
#         food.food_price = request.POST.get("food_price")
#         food.food_time = request.POST.get("food_time")
#         food.food_wight = request.POST.get("food_wight")
#         food.food_calories = request.POST.get("food_calories")
#         food.food_recipes = request.POST.get("food_recipes")
#         food.food_group = request.POST.get("food_group")
#         food.food_meal = request.POST.get("food_meal")
#         return redirect(request,"food/food/add.html")
#     return redirect(request,"food/food/add.html",{"recipes":Recipes.objects.all(),"food_group":FoodGroup.object.all(),"meal":Meal.objects.all()})
# def delete_food(request,id):
#     Food.objects.filter(id=id).delete()
#     return redirect(request,"food/food/show.html")
# def edit_food(request,id):
#     return redirect(request,"food/food/show.html")

# def set_cookie(request):
#     response = render(request,"cookietest/page1.html")
#     response.set_cookie(key='name',value='Soren',max_age=2592000)
#     response.set_cookie(key='family',value='Shamloo',max_age=60)
#     response.set_cookie(key='age',value='14',max_age=60)
#     return response

# def get_cookie(request):
#     context = {}
#     if request.COOKIES.get("name"):
#         name = request.COOKIES['name']
#         family = request.COOKIES['family']
#         age = request.COOKIES['age']
#         context = {
#             "name": name,
#             "family": family,
#             "age": age,
#         }
#     return render(request,"cookietest/page2.html",context)

def show_similar_foods(request):
    try:
        similar_foods = Food.objects.filter(food_group=request.COOKIES.get('food_group_id'))
        return render(request,"food/food/show_similar_foods.html",{'similar_foods':similar_foods})
    except:
        pass

def show_food(request,slug):
    try:
        food = Food.objects.get(food_slug=slug)
        food.food_views = food.food_views +1
        food.save()
        mukbangs = Mukbang.objects.filter(food = food)
        response = render(request,'food/food/show.html',{"food":food,'slug':slug,'mukbangs':mukbangs})
        response.set_cookie(key='food_group_id',value=str(food.food_group.id),max_age=10000)
    except ObjectDoesNotExist:
        error(request,_("غذا پیدا نشد."),"error")
        return redirect("main_app:index")
    except:
        error(request,_("خطا در اجرای عملیات!!"))
        return redirect("main_app:index")
    return response

def show_food_info(request):
    slug = request.GET.get('food_slug') 
    slid_name = request.GET.get('slid_name')
    food= Food.objects.filter(food_slug=slug)[0]
    if slid_name == "show_info_food":
        return render(request,"food/food/partials/show_food_info.html",{'food':food})
    elif slid_name == "show_food_stuff_form":
        return render(request,"food/food/partials/show_food_stuff_form.html",{'food':food})
    elif slid_name == "show_food_comments":
        return render(request,"food/food/partials/food_comments.html",{'food':food,'slug':slug})
    else:
        error(request,_('خطا در اجرای عملیات!'),'error')
        return redirect("main_app:index")
def show_foods_g(request,group_id):
    foods= Food.objects.filter(food_group=group_id)
    paginator=Paginator(foods,15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'food/food/show_foods.html',{"page_obj":page_obj})
def show_foods(request):
    foods= Food.objects.all()
    page_object_number = 12
    paginator=Paginator(foods,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'food/food/show_foods.html',{"page_obj":page_obj,'obj_len':len(foods),'page_object_number':page_object_number})
# FoodGroup Class
def add_food_group(request):
    if request.method == "POST":
        food_group = FoodGroup()
        food_group.group_name = request.POST['group_name']
        food_group.group_image = request.POST['group_image']
        return redirect(request,"food/food_group/add.html")
    return redirect(request,"food/food_group/show_groups.html")
def delete_food_group(request):
    FoodGroup.objects.filter(id=id).delete()
    return redirect(request,"food/food/show.html")
def edit_food_group(request,id):
    return redirect(request,"food/food/show.html")
def show_food_groups(request):
    return render(request,"food/food_group/show.html",{"food_groups":FoodGroup.objects.all()})

def show_group_food(request,group):
    foods = Food.objects.all()
    context = {"foods":foods,"group":group}
    return render(request,"",context)
#StuffGroup Class
def add_stuff_group(request):
    if request.method == "POST":
        stuff_group=StuffGroup()
        stuff_group.group_name = request.POST["group_name"]
        stuff_group.group_image = request.POST["group_image"]
        return redirect(request,"food/food/show.html")
    return render(request,"food/food/show.html")
def delete_stuff_group(request):
    StuffGroup.objects.get(id=id).delete()
    return render(request,"food/food/show.html")
def edit_stuff_group(request,id):
    return render(request,"food/food/show.html",{"stuff":StuffGroup.objects.get(id=id)})
def show_all_stuff_group(request):return redirect(request,"food/food/show.html",{"stuffs":StuffGroup.objects.all()})
# Stuff Class
def add_stuff(request):
    if request.method == "POST":
        stuff=Stuff()
        stuff.group_name = request.POST["group_name"]
        stuff.stuff_price = request.POST["stuff_price"]
        stuff.stuff_group = request.POST["stuff_group"]
        return redirect(request,"food/food/show.html")
    return render(request,"food/food/show.html",{"stuff_group":StuffGroup.objects.all()})
def delete_stuff(request):
    StuffGroup.objects.get(id=id).delete()
    return render(request,"food/food/show.html")
def edit_stuff(request,id):
    return render(request,"food/food/show.html",{"stuff":StuffGroup.objects.get(id=id)})
def show_all_stuff(request):return redirect(request,"food/food/show.html",{"stuffs":StuffGroup.objects.all()})
# Recipes Class
def add_recipes(request):
    if request.method == "POST":
        recipe = Recipes()
        recipe.recipes_image = request.POST['recipes_image']
        recipe.recipes_name = request.POST['recipes_name']
        recipe.recipes_stuffs = request.POST['recipes_stuffs']
        recipe.recipes =request.POST['recipes']
        recipe.save()
        return redirect(request,"food/recipe/show.html")
    return render(request,"food/recipe/show.html",{"stuffs":StuffGroup.objects.all()})
def delete_recipes(request):
    StuffGroup.objects.filter(id=id).delete()
    return render(request,"food/recipe/show.html")
def edit_recipes(request,id):
    return render(request,"food/recipe/show.html")
def show_recipes(request,slug):
    try:
        recipe=Recipes.objects.get(recipe_slug=slug)
    except ObjectDoesNotExist:
        error(request,_("مقاله پیدا نشد!"))
        return redirect("main_app:index")
    recipe.recipe_short_url = f"{settings.URL}food/recipe/{recipe.id}"
    recipe.recipe_views = recipe.recipe_views + 1
    recipe.save()
    return render(request,"food/recipe/show.html",{"recipe":recipe,"model":"recipe","slug":slug})
def show_recipe_with_id(request,id):
    recipe = Recipes.objects.get(id=id)
    recipe.recipe_views = recipe.recipe_views + 1
    recipe.save()
    return render(request,"food/recipe/show.html",{"recipe":recipe,"model":"recipe","slug":recipe.recipe_slug})

def add_like_recipe(request):
    if request.method == "POST":
        recipe_id = request.POST.get("recipe_id")
        print("ok")
        try:
            recipe = Recipes.objects.get(id=recipe_id)
            recipe.recipe_likes = recipe.recipe_likes+1
            recipe.save()
            return HttpResponse(recipe.recipe_likes)
        except ObjectDoesNotExist:
            return HttpResponse('دستور غذا پیدا نشد.')
        except:
            return HttpResponse(_("خطا در اجرای عملیات!"))

def add_dislike_recipe(request):
    if request.method == "POST":
        recipe_id = request.POST.get("recipe_id")
        try:
            recipe = Recipes.objects.get(id=recipe_id)
            recipe.recipe_dislikes = recipe.recipe_dislikes+1
            recipe.save()
            return HttpResponse(recipe.recipe_dislikes)
        except ObjectDoesNotExist:
            return HttpResponse('دستور غذا پیدا نشد.')
        except:
            return HttpResponse(_("خطا در اجرای عملیات!"))
        
        
        
        
def show_all_recipes(request): 
    recipes=Recipes.objects.all()
    paginator=Paginator(recipes,24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"food/recipe/show_recipes.html",{"page_obj":page_obj,'obj_len':len(recipes)})
def what_food(request):
    return render(request,"food/what_food/what_food.html")
def show_comments(request):
    return render(request,'food/food/partials/comments.html')
def add_to_my_recipes(request):
    if request.method == "POST":
        stuff_ids = request.POST.get('stuff_ids').split(',')
        food= Food.objects.get(id=request.POST.get('food_id'))
        sum_price = 0
        del stuff_ids[len(stuff_ids)-1]
        stuff_objects = []
        for stuff_id in stuff_ids:
            stuff_object  = Stuff.objects.get(id=stuff_id)
            sum_price +=(int(stuff_object.stuff_price) // 2)
            stuff_objects.append(stuff_object)
        sum_price+=(int(food.profit) + 3000)
        my_recipes_object = MyRecipes(recipes_food=food, recipes_user=request.user,recipes_name=request.POST.get('recipe_name'),recipes_price = sum_price)
        my_recipes_object.save()
        my_recipes_object.recipes_stuffs.set(stuff_objects)
        return HttpResponse("دستور شما با موفقیت ذخیره شد.")

def update_my_recipe(request):
    
        stuff_ids = request.POST.get('stuff_ids').split(',')
        food= Food.objects.get(id=request.POST.get('food_id'))
        sum_price = 0
        del stuff_ids[len(stuff_ids)-1]
        stuff_objects = []
        for stuff_id in stuff_ids:
            stuff_object  = Stuff.objects.get(id=stuff_id)
            sum_price +=(int(stuff_object.stuff_price) // 2)
            stuff_objects.append(stuff_object)
        sum_price+=(int(food.profit) + 3000)
        my_recipes_object = MyRecipes.objects.get(id=request.POST.get("recipe_id"),recipes_food=food,recipes_user=request.user)
        my_recipes_object.recipes_price=sum_price
        my_recipes_object.save()
        my_recipes_object.recipes_stuffs.set(stuff_objects)
        return HttpResponse("دستور شما با موفقیت آپدیت شد.")
def delete_my_recipe(request):
    if request.method == "POST":
        food= Food.objects.get(id=request.POST.get('food_id'))
        recipe_id=request.POST.get("recipe_id")
        my_recipe=MyRecipes.objects.get(id=recipe_id,recipes_food=food,recipes_user=request.user)
        try:
            MyRecipeCart(request).delete_from_my_recipe_cart(my_recipe)
        except:
            print()
        my_recipes_name = my_recipe.recipes_name
        my_recipe.delete()
        success(request,_(f"دستور غذای {my_recipes_name} با موفقیت حذف شد."),"success")
        return redirect("food_app:show_my_recipes")

def show_my_recipes(request):
    my_recipes=MyRecipes.objects.filter(recipes_user=request.user)
    page_object_number = 12
    paginator=Paginator(my_recipes,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'food/my_recipes/show_recipes.html',{"page_obj":page_obj,'obj_len':len(my_recipes),'page_object_number':page_object_number})


def show_my_recipe(request,recipe_id):
    try:
        recipe = MyRecipes.objects.get(id=recipe_id)
    except :
        error(request,_("دستور پیدا نشد!"),"error")
        return redirect("main_app:index")
    return render(request,"food/my_recipes/show_recipe.html",{"recipe":recipe}) 