from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import CustomUser,Customer,Country,State,City
from django.utils.translation import gettext_lazy as _
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display=('show_short_image_profile','mobile_number','email','name','family','is_active','is_admin','is_support')
    list_filter=('is_active','is_admin','family','is_support')
    fieldsets=(
        (None,{'fields':('mobile_number','password')}),
        (_('اطلاعات شخصی'),{'fields':('email','name','family','gender','address','birth_date','national_code','active_code','gifts','country','state','city','latitude_location','longitude_location')}),
        (_('مجوزها'),{'fields':('is_active','is_admin','is_support','is_superuser','is_serviceman','is_delivery','groups','user_permissions')}),
    )
    add_fieldsets=(
        (None,{'fields':('mobile_number','email','name','family','gender','password','re_password')}),      
    )
    search_fields=('mobile_number','name','family','country')
    ordering = ('mobile_number','family')
    filter_horizontal=('groups','user_permissions','gifts')
    raw_id_fields = ("country",'state','city')
    readonly_fields= ('show_short_image_profile',)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user","phone_number")
    list_filter = ("user","phone_number")
    search_fields = ("user","phone_number")
    raw_id_fields = ("country",'state','city')
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name","photo_of_the_flag","telephone_code")
    search_fields = ("name","photo_of_the_flag","telephone_code")
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name","country")
    search_fields = ("name","country")
    raw_id_fields = ("country",)
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",'country')
    search_fields = ("name",)
    raw_id_fields = ("country",)