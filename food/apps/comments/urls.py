# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="comments_app"
urlpatterns = [
    path('create-comment/<slug:slug>/<str:model>/', CommentView.as_view(), name="create_comment"),
    path('show-my-comments/', show_my_comments, name="show_my_comments"),
]