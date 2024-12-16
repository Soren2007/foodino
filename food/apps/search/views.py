# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from apps.food.models import Food
from apps.blog.models import Article,Author
from django.views.decorators.csrf import requires_csrf_token
from googletrans import Translator
# Create your views here. 
class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        translator=Translator()
        query = self.request.GET.get('q')
        new_query = translator.translate(query,dest=f'fa').text
        foods = Food.objects.filter(Q(food_name__icontains=new_query) | Q(food_description__icontains=new_query))
        blogs = Article.objects.filter(Q(article_title__icontains=new_query) | Q(article_group__icontains=new_query))
        authors = Author.objects.filter(Q(author_name__icontains=new_query) | Q(author_family__icontains=new_query) | Q(author_fullname__icontains=new_query))
        context = {'foods_obj': foods,'blogs_obj':blogs,'authors_obj':authors,'query':query}
        return render(request, 'search/results.html',context)