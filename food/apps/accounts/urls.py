from django.urls import path
from .views import *
app_name="accounts_app"
urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('compile-information/',CompileInformation,name='compile_information'),
    path('verify/',VerifyRegisterCodeView.as_view(),name='verify'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('user-panel/',user_panel,name='user_panel'),
    path('change-password/',ChangePasswordView.as_view(),name='change_password'),
    path('remember-password/',RememberPasswordView.as_view(),name='remember_password'),
    path('change-profile/',change_profile,name='change_profile'),
    path('show-my-gifts/',show_my_gifts,name='show_my_gifts'),
    path('show-my-messages/',show_my_messages,name='show_my_messages'),
    path('show-my-transactions/',show_my_transactions,name='show_my_transactions'),
    path('change-profile-and-full-name/',change_profile_and_full_name,name='change_profile_and_full_name'),
    path('save-location/',save_location,name='save_location'),
]