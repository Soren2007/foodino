# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='main_app'
urlpatterns = [
    path('', index,name='index'),
    path('about-me/', about_me,name='about_me'),
    path('rules/', rules,name='rules'),
    path('show-frequently-asked-questions/', show_frequently_asked_questions,name='show_frequently_asked_questions'),
    path('download/<str:content_type>/<str:file_path>/', download,name='download'),
    path('save-image/', save_image,name='save_image'),   
]

# handler404 = 'apps.main.views.http_status_404'