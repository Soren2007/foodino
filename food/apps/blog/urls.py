# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="blog_app"
urlpatterns = [
    path('add-key-word/', add_key_word, name="add_key_word"),
    path('delete-key-word/<int:id>/', add_key_word, name="delete_key_word"),
    path('edit-key-word/<int:id>/', edit_key_word, name="edit_key_word"),
    path('show-key-word/<int:id>/', show_key_word, name="show_key_word"),
    path('show-key-words/', show_key_words, name="show_key_words"),
    
    path('add-blog/', add_article, name="add_blog"),
    path('delete-blog/<str:slug>/', add_article, name="delete_blog"),
    path('edit-blog/<str:slug>/', edit_article, name="edit_blog"),
    path('show-blog/<str:slug>/', show_article, name="show_blog"),
    path('<int:id>/', show_article_with_id, name="show_article_with_id"),
    path('show-blogs/', show_all_article, name="show_blogs"),
    path('show-blogs-with-author//<str:author_slug>/', show_article_with_author, name="show_article_with_author"),
    
    path('add-author/', add_author, name="add_author"),
    path('delete-author/<str:slug>/', add_author, name="delete_author"),
    path('edit-author/<str:slug>/', edit_author, name="edit_author"),
    path('show-author/<str:slug>/', show_author, name="show_author"),
    path('show-authors/', show_all_author, name="show_authors"),
    
    
    path('add-like/', add_like, name="add_like"),
    path('add-dislike/', add_dislike, name="add_dislike"),
]