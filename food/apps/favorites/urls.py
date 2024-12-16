# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="favorites_app"
urlpatterns = [
    path('add-to-favorite/', add_to_favorite, name="add_to_favorite"),
    path('delete-to-favorite/', delete_to_favorite, name="delete_to_favorite"),
    path('add-to-favorite-blog/', add_to_favorite_blog, name="add_to_favorite_blog"),
    path('delete-to-favorite-blog/', delete_to_favorite_blog, name="delete_to_favorite_blog"),
    
    path('status-of-favorite/', status_of_favorite, name="status_of_favorite"),
    
    path('user-favorite/', UserFavoriteView.as_view(), name="user_favorite"),
] 