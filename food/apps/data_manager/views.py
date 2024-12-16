# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from apps.food.models import Food,Recipes,StuffGroup,Stuff,FoodGroup,FoodStuffType,Meal,MyRecipes
from apps.accounts.models import Country,City,CustomUser,Customer
from apps.blog.models import KeyWord,Author,Article
from apps.branch.models import Branch
from apps.comments.models import Comment
from apps.discounts.models import Coupon,DiscountBasket,DiscountBasketDetail
from apps.favorites.models import Favorite
from apps.message.models import Message,UserChatRoom,ChatRoom
# from apps.orders.models import PaymentType,Order,OrderDetails
from apps.payments.models import Payment,Currency
from apps.language.models import Language,LanguageFont
from django.conf import settings
from utils import Scrap,image_saver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import error,success
from os import mkdir
from datetime import date,datetime
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def create_or_update_languages(request):
    if request.user.is_authenticated and request.user.is_admin:
        objects = Scrap("https://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code",request).scrap_language()
        language_create_number = 0
        language_update_number = 0
        for object in objects:
            try:
                language = Language.objects.get(language_code=str(object['language_code']))
                language.language_code = str(object['language_code'])
                language.language_name = str(object['language_name'])
                language.language_directionality = object['language_directionality']
                language.save()
                language_update_number+=1
            except ObjectDoesNotExist:
                Language.objects.create(language_code=str(object['language_code']),language_name=str(object['language_name']),language_directionality=object['language_directionality'])
                language_create_number+=1
        success(request,f"{language_create_number} " + _("زبان اضافه شد.") + f" \t | \t {language_update_number}" + _("زبان آپدیت شد."),"success")
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")
    
def create_or_update_currency(request):
    if request.user.is_authenticated and request.user.is_admin:
        objects = Scrap("https://www.flytoday.ir/blog/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%D8%A8%D8%A7-%D9%88%D8%A7%D8%AD%D8%AF-%D9%BE%D9%88%D9%84-%DA%A9%D8%B4%D9%88%D8%B1%D9%87%D8%A7",request).scrap_currencies()
        currencies_create_number = 0
        currencies_update_number = 0
        for object in objects:
            print(object['country_name'])
            try:
                country = Country.objects.get(name=object['country_name'])
            except ObjectDoesNotExist:
                country = Country.objects.create(name=object['country_name'])
                country.save()
            try:
                currency = Currency.objects.get(country=country.id)
                currency.currency = str(object['currency'])
                currency.ISO_code = str(object['ISO_code'])
                currency.symbol = object['symbol']
                currency.save()
                currencies_update_number+=1
            except ObjectDoesNotExist:
                Currency.objects.create(country=country,currency=str(object['currency']),ISO_code=object['ISO_code'],symbol=object['symbol'])
                currencies_create_number+=1
        success(request,f"{currencies_create_number} " + _("واحد پول اضافه شد.") + f" \t | \t {currencies_update_number}" + _("واحد پول آپدیت شد."),"success")
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")       
    
def create_or_update_country(request):
    if request.user.is_authenticated and request.user.is_admin:
        objects = Scrap("https://iraniju.ir/%D9%BE%DB%8C%D8%B4-%D8%B4%D9%85%D8%A7%D8%B1%D9%87-%DA%A9%D8%B4%D9%88%D8%B1%D9%87%D8%A7/",request).scrap_countries()
        country_create_number = 0
        country_update_number = 0
        for object in objects:
            try:
                country = Country.objects.get(name=str(object['name']))
                country.telephone_code=object['telephone_code']
                country.save()
                country_update_number+=1
            except ObjectDoesNotExist:   
                Country.objects.create(name=str(object['name']),telephone_code=object['telephone_code'])
                country_create_number+=1
            except:
                continue
        success(request,f"{country_create_number} " + _("کشور اضافه شد.") + f" \t | \t {country_update_number}" + _("کشور آپدیت شد."),"success")
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")       
        

def create_or_update_cities(request):
    if request.user.is_authenticated and request.user.is_admin:
        countries = Country.objects.all()
        if len(countries) != 0 :
            city_create_number = 0
            city_update_number = 0
            for country in countries:
                if str(country.name) == "ایران":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86",request).scrap_cities('.wikitable:not(wikitable:last-of-type) td:nth-child(1) a')
                
                elif str(country.name) == "آذربایجان":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%AC%D9%85%D9%87%D9%88%D8%B1%DB%8C_%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86",request).scrap_cities('.sortable th:nth-child(1) a')
                
                elif str(country.name) == "آفریقای مرکزی":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%AC%D9%85%D9%87%D9%88%D8%B1%DB%8C_%D8%A2%D9%81%D8%B1%DB%8C%D9%82%D8%A7%DB%8C_%D9%85%D8%B1%DA%A9%D8%B2%DB%8C",request).scrap_cities('.prettytable td:nth-child(2) a')
                
                elif str(country.name) == "آلمان":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A2%D9%84%D9%85%D8%A7%D9%86_%D8%A8%D8%B1_%D9%BE%D8%A7%DB%8C%D9%87_%D8%AC%D9%85%D8%B9%DB%8C%D8%AA",request).scrap_cities('.wikitable td:nth-child(2) a:last-of-type')
                    
                elif str(country.name) == "اردن":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%D8%B1%D8%AF%D9%86",request).scrap_cities('.prettytable td:nth-child(2) a')
                elif str(country.name) == " استرالیا":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%D8%B3%D8%AA%D8%B1%D8%A7%D9%84%DB%8C%D8%A7",request).scrap_cities('.prettytable td:nth-child(2) a')
                elif str(country.name) == "اطریش":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%D8%AA%D8%B1%DB%8C%D8%B4",request).scrap_cities('.wikitable td:nth-child(2) a:last-of-type')
                elif str(country.name) == "الجزایر":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%DB%8C%D8%B1",request).scrap_cities('.prettytable td:nth-child(2) a')
                elif str(country.name) == "الجزایر":
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D8%A7%D9%84%D8%B3%D8%A7%D9%84%D9%88%D8%A7%D8%AF%D9%88%D8%B1#:~:text=%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C%20%D9%85%D9%87%D9%85%20%D8%A2%D9%86%20%D8%B3%D8%A7%D9%86%20%D8%B3%D8%A7%D9%84%D9%88%D8%A7%D8%AF%D9%88%D8%B1,%D9%88%DB%8C%D8%B1%D8%A7%D9%86%DA%AF%D8%B1%20%D9%88%20%D9%81%D9%88%D8%B1%D8%A7%D9%86%E2%80%8C%D9%87%D8%A7%DB%8C%20%D8%A2%D8%AA%D8%B4%D9%81%D8%B4%D8%A7%D9%86%DB%8C%20%D8%A8%D9%88%D8%AF%D9%87%E2%80%8C%D8%A7%D8%B3%D8%AA.",request).scrap_cities('table[class="navbox"] td:nth-child(2) a') # no object

                else:
                    objects = Scrap(f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_{country.name}",request).scrap_cities()
                if objects:     
                    for object in objects:
                        try:
                            City.objects.get(name=str(object['city_name']))
                            city_update_number+=1
                        except ObjectDoesNotExist:   
                            City.objects.create(name=str(object['city_name']),country=country)
                            city_create_number+=1
                        except:
                            continue
        else:
            error(request,"کشوری وجود ندارد ابتدا کشورها را وارد کنید.","error")
            return redirect("")
            
        success(request,f"{city_update_number}"+ _("شهر اضافه شد.") + f" \t | \t {city_create_number}"+ _("شهر اضافه شد."),"success")
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")       

def create_stuff_object(object,stuff_group):
    try:
        print(100*"-")
        print(object['stuff_image_url'])
        image_saver(object['stuff_image_url'][0],f"{settings.BASE_DIR}/media/images/food/stuffs/",object['stuff_name'],".jpg")
        Stuff.objects.create(stuff_name=str(object['stuff_name']),stuff_price=object['stuff_price'],stuff_image=f"/images/food/stuffs/{object['stuff_name']}.jpg",stuff_group=stuff_group)
    except :
        Stuff.objects.create(stuff_name=str(object['stuff_name']),stuff_price=object['stuff_price'],stuff_image=f"/images/food/stuffs/none.jpg",stuff_group=stuff_group)
def update_stuff_object(stuff_name,stuff_price):
    stuff = Stuff.objects.get(stuff_name=stuff_name)
    if stuff.stuff_price_auto == True:
        stuff.stuff_price=stuff_price
        stuff.save()
def create_or_update_stuffs_and_foods_price(request):
    if request.user.is_authenticated and request.user.is_admin:
        creates_group_number = 0
        creates_stuff_number = 0
        updates_stuff_number = 0
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%85%DB%8C%D9%88%D9%87-%D9%88-%D8%B3%D8%A8%D8%B2%DB%8C%D8%AC%D8%A7%D8%AA~Category~30249",request).scrap_stuffs()
        except:
            error(request,"خطا در اجرای عملیات!","error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="میوه و سبزیجات")
        except ObjectDoesNotExist:
            stuff_group=StuffGroup.objects.create(group_name="میوه و سبزیجات")
            creates_group_number+=1
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%A2%D8%AC%DB%8C%D9%84-%D9%88-%D8%AE%D8%B4%DA%A9%D8%A8%D8%A7%D8%B1~Category~30250",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="آجیل و خشکبار")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="آجیل و خشکبار")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%BA%D9%84%D8%A7%D8%AA-%D9%88-%D8%AD%D8%A8%D9%88%D8%A8%D8%A7%D8%AA~Category~30256",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="غلات و حبوبات")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="غلات و حبوبات")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%82%D9%86%D8%A7%D8%AF%DB%8C~Category~30261",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="قنادی")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="قنادی")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue   
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%84%D8%A8%D9%86%DB%8C%D8%A7%D8%AA~Category~30267",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="لبنیات")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="لبنیات")
            creates_group_number+=1
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:    
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%85%D9%88%D8%A7%D8%AF-%D9%BE%D8%B1%D9%88%D8%AA%D8%A6%DB%8C%D9%86%DB%8C~Category~36093",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="پروتئینی")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="پروتئینی")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%A2%D8%A8%D9%84%DB%8C%D9%85%D9%88%D8%8C-%D8%B3%D8%B1%DA%A9%D9%87-%D9%88-%D8%AA%D8%B1%D8%B4%DB%8C%D8%AC%D8%A7%D8%AA~Category~30270",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="آبلیمو، سرکه و ترشیجات")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="آبلیمو، سرکه و ترشیجات")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
            
        objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%86%D8%A7%D9%86~Category~2101",request).scrap_stuffs()
        try:
            stuff_group=StuffGroup.objects.get(group_name="نان")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="نان")
            creates_group_number+=1
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%A7%D8%AF%D9%88%DB%8C%D9%87-%D8%AC%D8%A7%D8%AA~Category~30272",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="ادویه جات")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="ادویه جات")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue  
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%86%D9%88%D8%B4%DB%8C%D8%AF%D9%86%DB%8C-%D9%87%D8%A7~Category~30247",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="نوشیدنی ها")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="نوشیدنی ها")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%B1%D9%88%D8%BA%D9%86~Category~30276",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="روغن خوراکی")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="روغن خوراکی")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%B1%D8%A8-%D9%88-%D8%B3%D8%B3~Category~30274",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="رب و سس")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="رب و سس")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%82%D9%86%D8%AF-%D9%88-%D8%B4%DA%A9%D8%B1~Category~30275",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="قند و شکر")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="قند و شکر")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%BE%D8%A7%D8%B3%D8%AA%D8%A7~Category~35456",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="پاستا")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="پاستا")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D8%A7%D8%B1%D8%AF%D9%87-%D9%88-%D8%B4%DB%8C%D8%B1%D9%87~Category~36092",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="ارده و شیره")
        except ObjectDoesNotExist:  
            stuff_group=StuffGroup.objects.create(group_name="ارده و شیره")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        try:
            objects = Scrap("https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%BE%D9%88%D8%B1%D9%87-%D9%85%DB%8C%D9%88%D9%87-%D9%88-%D8%B3%D8%A8%D8%B2%DB%8C%D8%AC%D8%A7%D8%AA~Category~46955",request).scrap_stuffs()
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        try:
            stuff_group=StuffGroup.objects.get(group_name="پوره میوه و سبزیجات")
        except ObjectDoesNotExist:
            stuff_group=StuffGroup.objects.create(group_name="پوره میوه و سبزیجات")
            creates_group_number+=1
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
        for object in objects:
            try:
                update_stuff_object(str(object['stuff_name']),object['stuff_price'])
                updates_stuff_number+=1
            except ObjectDoesNotExist:    
                create_stuff_object(object=object,stuff_group=stuff_group)
                creates_stuff_number+=1
            except:
                continue
        number_food_update_price = 0
        for food in Food.objects.all():
            if food.is_auto_compile_price == True:
                stuff_sum_price = 0
                for stuff in food.food_recipes.recipe_stuffs.all():
                    stuff_sum_price+=(int(stuff.stuff_price) // 2)
                food.food_price = stuff_sum_price + food.profit
                food.save()
                number_food_update_price+=1
        success(request,f"{creates_group_number} " + _("گروه اضافه شد.")+ f"\t | \t{creates_stuff_number} " + _("ماده اضافه شد.") + f"\t | \t{updates_stuff_number} " + _("ماده آپدیت شد.") + f"\t | \t {number_food_update_price}" + _("غذا آپدیت شد") ,"success")
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")    

from re import findall
from apps.accounts.models import *
from apps.accounts.models import *
from apps.reservation.models import *
from apps.scores.models import *
def create_csv_model(model,request):
    if request.user.is_authenticated and request.user.is_admin:
        csv = ""
        objects = model.objects.all()
        if len(objects) != 0:
            class_name=model.class_name
            date_now = date.today()
            object_number = 0
            for object in objects:
                csv_header = ""
                csv_data = ""
                for data in model.fields_information(object):
                    csv_header += f"{data['verbose_name']}\t"
                    csv_data += f"{data['value']}\t"
                if object_number == 0:
                    csv+=csv_header+"\n"+csv_data+"\n"
                else:
                    csv+=csv_data+"\n"
                object_number+=1
            dir_csv_file = f"{settings.BASE_DIR}\\media\\files\\csv\\{date_now}"
            try:
                mkdir(dir_csv_file)
            except:
                print("")
            with open(dir_csv_file+f"\\{class_name}.csv",'w',encoding="UTF-16") as csv_file:
                csv_file.write(csv)
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  
from os import listdir
def get_data_and_save_csv_format(request):
    if request.user.is_authenticated and request.user.is_admin:
        try:
            class_names = []
            path = f"{settings.BASE_DIR}\\apps\\"
            for app_name in listdir(path):
                with open(f"{path}{app_name}//models.py", "r",encoding="UTF-8") as model_file:
                    class_names = findall(r"class (.*)\(.*\).*:",model_file.read())
                    if len(class_names) > 0:
                        for class_name in class_names:
                            if class_name != "CustomUserManager":
                                eval(f"create_csv_model({class_name},request)")
            success(request,"دیتا با موفقیت ذخیره شد.","success")
            return redirect("data_manager_app:index")
        except Exception as error:
            error(request,error,"error")
            print(error)
            return redirect("data_manager_app:index")  
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")
  
def create_statistic_data(request,chart_title):
    year=date.today().year
    month=date.today().month
    day=date.today().day
    path = f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{chart_title}\\data\\{year}"
    try:
        mkdir(path)
    except Exception as error:
        print(error)
    try:
        mkdir(f"{path}\\month\\{month}")
    except Exception as error:
        print(error)    
    try:
        mkdir(f"{path}\\month\\{month}\\day")
    except Exception as error:
        print(error)    
    try:
        mkdir(f"{path}\\month\\{month}\\day\\{day}")
    except Exception as error:
        print(error)
        
    with open(f"{path}\\month\\{month}\\day\\{day}\\{date.today()}.csv",'w',encoding="UTF-8") as file:
        Food.objects.all()
        row_number=1
        csv_string = "row,month,food name,food views,sel\n"
        for food in Food.objects.all():
            csv_string+=f"{row_number},{month},{food.food_name},{food.food_views},{food.food_sales_number}\n"
            row_number+=1
        file.write(str(csv_string))  

CHART_TITLES = [('food_views','تعداد بازدید کنندگان غذا'),('food_comments','تعداد نظرات غذا'),('food_sales_number','تعداد خرید غذا'),('blog_views','تعداد بازدید کنندگان مقاله'),('blog_comments','تعداد نظرات مقاله'),('blog_liks','تعداد تایید کنندگان مقاله')]
from utils import Plot
from os import chdir
from pandas import read_csv
from matplotlib.pyplot import *
from django.http import HttpRequest    
def show_plot(request,year=date.today().year):
    if request.user.is_authenticated and request.user.is_admin:
        year=request.GET.get("year")
        month=request.GET.get("month")
        day=request.GET.get("day")
        chart_title = request.GET.get('chart_title')
        create_statistic_data(request,chart_title)
        dir = f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{chart_title}\\data\\{year}"
        path = f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{chart_title}\\plots\\{year}"
        try:
            mkdir(path)
            mkdir(f"{path}\\month")
        except Exception as error:
            print()
        try:
            mkdir(f"{path}\\month\\{month}")
            mkdir(f"{path}\\month\\{month}\\day")
        except Exception as error:

            print()
        try:
            mkdir(f"{path}\\month\\{month}\\day\\{day}")
        except Exception as error:
            print()
        try:
            mkdir(f"{path}\\month\\{month}\\day\\{day}")
        except Exception as error:
            print()
        try:
            if len(month)==1:
                new_month = f"0{month}"
            if len(day)==1:
                new_day = f"0{day}"
            else:
                new_day = f"{day}"  
            data =  read_csv(f"{dir}\\month\\{month}\\day\\{day}\\{year}-{new_month}-{new_day}.csv") 
        except Exception as error:
            print(error)
            # error(request,error,"error")
            # return redirect("data_manager_app:index")
        chdir(f"{path}\\month\\{month}\\day\\{day}")
        style.use('ggplot')
        xlabel("Month")
        ylabel("Views")
        title("Food Views")
        if request.GET.get('chart_model') == "bar":
            bar(data['month'],data['food views'],color=request.GET.get('color'),label=f'Food View at {year}')
        else:
            plot(data['month'],data['food views'],color=request.GET.get('color'),label=f'Food View at {year}',marker='o',ms=4,mfc=request.GET.get('color_dot'),mec=request.GET.get('color_dot'),linewidth=1)
        legend()
        image_name = f'food_view_plote_on_{year}_{month}_{day}({request.GET.get("show_chart_number")})'
        savefig(image_name)
        close()
        return render(request,"data_manager/partials/show_plot.html",{"image_address":f"\\media\\files\\data_statistics\\{chart_title}\\plots\\{year}\\month\\{month}\\day\\{day}\\{image_name}.png"})
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")
def update_data(request):
    if datetime.now().hour == 6 and datetime.now().minute == 0:
        try:
            create_or_update_stuffs_and_foods_price(request)
            create_or_update_country(request)
            create_or_update_cities(request)
            get_data_and_save_csv_format(request)
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("data_manager_app:index")
    return {"waring":_("سایت درحال آپدیت شدن می باشد.")}

def index(request):
    if request.user.is_authenticated and request.user.is_admin:
        languages = Language.objects.all()
        return render(request,"data_manager/index.html",{"chart_titles":CHART_TITLES,'languages':languages})
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")
def show_years_with_chart_title(request):
    chart_title = request.GET.get('chart_title')
    create_statistic_data(request,chart_title)
    years=listdir(f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{request.GET.get('chart_title')}\\data")
    return render(request,"data_manager/partials/show_years.html",{"years":years})
def show_months_with_year(request):
    chart_title = request.GET.get('chart_title')
    create_statistic_data(request,chart_title)
    months=listdir(f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{request.GET.get('chart_title')}\\data\\{request.GET.get('year')}\\month")
    return render(request,"data_manager/partials/show_months.html",{"months":months})
def show_days_with_month(request):
    chart_title = request.GET.get('chart_title')
    create_statistic_data(request,chart_title)
    days=listdir(f"{settings.BASE_DIR}\\media\\files\\data_statistics\\{request.GET.get('chart_title')}\\data\\{request.GET.get('year')}\\month\\{request.GET.get('month')}\\day")
    return render(request,"data_manager/partials/show_days.html",{"days":days})
        
def update_or_create_messages_language(request):
    if request.user.is_authenticated and request.user.is_admin:
        create_language_folder_and_files()
        translate_messages()
        return HttpRequest('ok')
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")

from apps.event.models import Event
from utils import send_sms,send_mail
from random import randint
def send_sms_message_for_event(request):
    if request.user.is_authenticated and request.user.is_admin:
        events = Event.objects.filter(event_is_active = True)
        if len(events) > 0: 
            event = events[randint(0,len(events)-1)]
            for user in CustomUser.objects.all():
                send_sms(request,user.mobile_number,event.event_text,redirect_name="data_manager:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")

def send_email_message_for_event(request):
    if request.user.is_authenticated and request.user.is_admin:
        events = Event.objects.filter(event_is_active = True)
        if len(events) > 0:
            event = events[randint(0,len(events)-1)]
            emails = (user.email for user in CustomUser.objects.all())
            send_mail(event.event_title,event.event_text,'info@foodino.com',emails) 
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  
       
# translate_messages()

def create_or_update_css_fonts(request):
    if request.user.is_authenticated and request.user.is_admin:
        for language_font in LanguageFont.filter(is_active=True):
            css_string="@font-face {font-family:" + language_font.font_name + ";src:url('" + language_font.font_embedded_opentype_format + ") format('embeddad-opentype'),url('" + language_font.font_truetype_format + "') format('truetype'),url('" + language_font.font_woff_format + "') format('woff'),url('" + language_font.font_woff_2_format + "') format('woff2')}"
            css_font_file_path = f'{settings.BASE_DIR}/static/css/fonts/{language_font.language.language_code}/{language_font.font_name}.css'
            if not exists(css_font_file_path):
                with open(css_font_file_path,'w') as font_css_file:
                    font_css_file.write(css_string)
            else:
                with open(css_font_file_path,'x') as font_css_file:
                    font_css_file.write(css_string)
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  

from PIL import Image
def convert_image_format_to_webp(request):
    if request.user.is_authenticated and request.user.is_admin:
        for dir in listdir(f"{settings.MEDIA_URL}/images/"):    
            image = Image.open(import_file_path)
            image.save(export_file_path)
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  
        
from utils import Translator_Language
def language_with_lang_code(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST":
            language_code = request.POST.get("language_code")
            translator=Translator_Language(language_code)
            translator.translate_po_files()
            translator.translate_values_of_models()
            translator.compilemessages(language_code)
            return HttpResponse(_("با موفقیت انجام شد."))
    return HttpResponse(_("شما نمیتوانید وارد این صفحه شوید!")) 
        
def language_with_lang_codes(request):
    if request.user.is_authenticated and request.user.is_admin:
        for language in Language.objects.all():
            translator=Translator_Language(language.language_code)
            translator.translate_po_files()
            translator.translate_values_of_models()
            translator.compilemessages(language.language_code)
        success(request,_("با موفقیت انجام شد."))
        return redirect("data_manager_app:index")
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  