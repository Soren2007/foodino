# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from apps.food.models import Stuff,Recipes
from django.views import View
from django.contrib.messages import success,error,warning
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from googletrans import Translator
stuff_list=[] 
# Create your views here.
def index(request):
    return render(request,'what_cook/index.html')
def show_recipes(request):
    if request.method == "POST":
        translator=Translator()
        stuff_names = request.POST.get("stuff_names")
        stuff_names=stuff_names.split(',')
        print(stuff_names)
        del stuff_names[len(stuff_names)-1]
        stuff_ids =[]
        for stuff_name in stuff_names:
            stuff_name=translator.translate(stuff_name,dest=f'fa').text
            for stuff in Stuff.objects.filter(Q(stuff_name__icontains=stuff_name)):
                stuff_ids.append(stuff.id)
        print(stuff_ids)
        recipes=Recipes.objects.filter(Q(recipe_stuffs__in=stuff_ids))
        return render(request,"what_cook/partials/show_recipes.html",{"recipes_o":recipes})
    return redirect("what_cook_app:show_recipes")