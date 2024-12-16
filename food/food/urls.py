# File version
__version__ = "1.1.1"
# File Description
"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('scores/', include("apps.scores.urls",namespace="scores_app")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

urlpatterns+=i18n_patterns(
    path('', include("apps.message.urls",namespace="message_app")),
    path('favorites/', include("apps.favorites.urls",namespace="favorites_app")),
    path('my-environment/', include("apps.my_environment.urls",namespace="my_environment_app")),
    path('data-manager/', include("apps.data_manager.urls",namespace="data_manager_app")),
    path('event/', include("apps.event.urls",namespace="event_app")),
    path('language/', include("apps.language.urls",namespace="language_app")),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('', include("apps.main.urls",namespace="main_app")),
    path('food/', include("apps.food.urls",namespace="food_app"),name="food_app"),
    path('blog/', include("apps.blog.urls",namespace="blog_app"),name="blog_app"),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('rosetta/', include('rosetta.urls')),
    path('orders/', include("apps.orders.urls",namespace="orders_app")),
    path('accounts/', include("apps.accounts.urls",namespace="accounts_app")),
    path('search/', include("apps.search.urls",namespace="search_app")),
    path('discounts/', include("apps.discounts.urls",namespace="discounts_app")),
    path('payment/', include("apps.payments.urls",namespace="payments_app")),
    path('what-cook/', include("apps.what_cook.urls",namespace="what_cook_app")),
    path('comments/', include("apps.comments.urls",namespace="comments_app")),
    path('ads/', include("apps.ad.urls",namespace="ad_app")),
    path('subscription/', include("apps.subscription.urls",namespace="subscription_app")),
    path('mukbang/', include("apps.mukbang.urls",namespace="mukbang_app")),
    path('gift/', include("apps.gift.urls",namespace="gift_app")),
    path('chat-gpt/', include("apps.chat_gpt.urls",namespace="chat_gpt_app")),
    # path('', include("googleauthentication.urls")),
    path('accounts/auth/', include("allauth.urls")),
    path('delivery/', include("apps.delivery.urls",namespace="delivery_app")),
)
    
handler404 = 'apps.main.views.http_status_404'
admin.site.site_header = _("پنل مدیریت سایت فودینو")
# admin.site.site_title = "صفحه اصلی"
admin.site.index_title = _("به پنل مدیریت سایت فودینو خوش آمدید.")