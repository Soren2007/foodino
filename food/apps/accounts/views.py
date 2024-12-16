from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterUserForm,VerifyRegisterCodeForm,LoginUserForm,ChangePasswordForm,RememberPasswordForm
from utils import create_random_code,send_sms
from .models import CustomUser,Customer
from apps.payments.models import Payment
from django.contrib.messages import success,error
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from os.path import basename
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.conf import settings
from os.path import isfile
from os import remove
from django.utils.translation import gettext_lazy as _
# Create your views here.

class RegisterUserView(View):
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('main_app:index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request,'accounts/register.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        try: 
            CustomUser.objects.get(mobile_number=data['mobile_number'])
        except ObjectDoesNotExist:
                active_code= create_random_code(5)
                if send_sms(request,data['mobile_number'],f'welcome to foodino site\ncode: {active_code}',"accounts_app:register") == 200:
                    CustomUser.objects.create_user(
                        mobile_number=data['mobile_number'],
                        active_code=active_code,
                        password=data['password']
                        )
                    request.session['user_session'] = {
                        'active_code': str(active_code),
                        'mobile_number':data['mobile_number'],
                        'remember_password':False
                    }
                    success(request,_('اطلاعات شما ثبت شد. کد فعال سازی را وارد کنید.'),'success')
                    return redirect('accounts_app:verify')
                return redirect('accounts_app:register')
        # except:
        #     error(request,'login','error')
        #     return redirect('accounts_app:register')    
           
        error(request,_('خطا در انجام ثبت نام'),'error')
        return redirect('accounts_app:register')    
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from os.path import splitext
def CompileInformation(request):
    if request.method == 'POST':
        phone_number=request.session['user_session']['mobile_number']
        user = CustomUser.objects.filter(mobile_number = phone_number)
        address = request.POST.get('address')
        imageUpload = request.FILES['profile']
        # print(request.POST['profile'])
        if imageUpload.size > 2000: #byt
            image_name,image_ext = splitext(imageUpload.name)
            current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            image_path = "images/profile/"+ image_name+current_time+image_ext
            user.update(
                name=request.POST.get('name'),
                family=request.POST.get('family'),
                email=request.POST.get('email'),
                birth_date=request.POST.get('birth_date'),
                national_code=request.POST.get('national_code'),
                postal_code=request.POST.get('postal_code'),
                # profile=image_path,
                gender=request.POST.get('gender'),
                address=address,
                is_complete_information=True,
            )
        # Customer.objects.create(
        #     user=user,
        #     phone_number = phone_number,
        #     address= address,
        #     image = request.POST.get('profile'),
        # )
            success(request,_('اطلاعات شما ثبت شد.'),'success')
            next_url=request.GET.get('next')
            if next_url is not None:
                return redirect(next_url)
            else:
                return redirect('main_app:index')
        else:
            error(request,_('عکس پروفایل نباید بیش از 2 مگابایت باشد!'),'error')
            return redirect('accounts_app:index')
    user = CustomUser.objects.get(mobile_number = request.session['user_session']['mobile_number'])
    if user.is_complete_information == True:
        request.session['user_session']['is_complete_information'] = True
        return render(request,'accounts/compile_information.html',{'user':user})
    return render(request,'accounts/compile_information.html')
class VerifyRegisterCodeView(View):
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('main_app:index')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = VerifyRegisterCodeForm()
        return render(request, 'accounts/verify_register_code.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = VerifyRegisterCodeForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user_session=request.session['user_session']
            if data['active_code'] == user_session['active_code']:
                user = CustomUser.objects.get(mobile_number=user_session['mobile_number'])
                if user_session['remember_password']==False:
                    user.is_active = True
                    user.active_code= create_random_code(5)
                    user.save()
                    success(request,'ثبت نام با موفقیت انجام شد.','success')
                    return redirect('main_app:index')
                else:
                    return redirect('accounts_app:change_password')
            else:
                error(request,_('کد فعال سازی وارد شده اشتباه می باشد.'),'error')
                return render(request, 'accounts/verify_register_code.html',{'form':form})
        error(request,'اطلاعات وارد شده معتبر نمی باشد.','error')
        return render(request, 'accounts/verify_register_code.html',{'form':form})

class LoginUserView(View):    
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('main_app:index')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'accounts/login.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(username=data['mobile_number'],password=data['password'])
            if user is not None:
                login(request,user)
                success(request,_('ورود با موفقیت انجام شد.'),'success')
                request.session['user_session'] = {
                    'mobile_number':data['mobile_number'],
                    }
                next_url=request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('main_app:index')
            else:
                error(request,_('اطلاعات وارد شده نادرست است.'),'error')
                return render(request, 'accounts/login.html',{'form':form})
        else:
            error(request,'اطلاعات وارد شده نامعتبر است.','error')
            return render(request, 'accounts/login.html',{'form':form})
            
class LogoutUserView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        food_data_cart = request.session.get('food_data_cart')
        my_recipes_data_cart = request.session.get('my_recipes_data_cart')
        chat_session = request.session.get('chat_session')
        logout(request)
        request.session['food_data_cart'] = food_data_cart
        request.session['my_recipes_data_cart'] = my_recipes_data_cart
        request.session['chat_session'] = chat_session
        next_url=request.GET.get('next')
        if next_url is not None:
            return redirect(next_url)
        else:
            return redirect('main_app:index')

def user_panel(request):
    from apps.orders.models import Order
    last_orders = Order.objects.filter(customer=request.user.id).order_by("-register_date")[:20]
    return render(request, 'accounts/user_panel.html',{'last_orders':last_orders})
class ChangePasswordView(View):
    def get(self, request, *args,**kwargs):
        form = ChangePasswordForm()
        return render(request, 'accounts/change_password.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user_session=request.session['user_session']
            user=CustomUser.objects.get(mobile_number=user_session['mobile_number'])
            user.set_password(data['password'])
            user.active_code = create_random_code(5)
            user.save()
            success(request,_('رمز عبور شما با موفقیت تغییر کرد.'),'success')
            return redirect('accounts_app:login')
        else:
            error(request,_('اطلاعات وارد شده معتبر نمی باشد.'),'error')
            return render(request, 'accounts/change_password.html',{'form':form})
            
class RememberPasswordView(View):
    def get(self, request, *args,**kwargs):
        form = RememberPasswordForm()
        return render(request, 'accounts/remember_password.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = RememberPasswordForm(request.POST)
        if form.is_valid(): 
            try:
                data=form.cleaned_data
                user=CustomUser.objects.get(mobile_number=data['mobile_number'])
                active_code = create_random_code(5)
                user.active_code=active_code
                user.save()
                if send_sms(request,data['mobile_number'],f'foodino site\ncode: {active_code}',"accounts_app:remember_password") == 200:
                    request.session['user_session'] = {
                        'active_code': str(active_code),
                        'mobile_number':data['mobile_number'],
                        'remember_password':True
                    }
                    success(request,_('جهت تغییر رمز عبور خود کد دریافتی را ارسال کنید','success'))
                    return redirect('accounts_app:verify')
                return redirect("accounts_app:remember_password")
            except:
                error(request,_('شماره موبایل وارد شده موجود نمی باشد.'),'error')
                return redirect("accounts_app:remember_password")
                    
def change_profile(request):
    phone_number=request.session['user_session']['mobile_number']
    user = CustomUser.objects.filter(mobile_number = phone_number)
    user.update(
        profile=f"images/profile/{basename(request.GET.get('profile_address'))}"
    )
    next_url=request.GET.get('next')
    if next_url is not None:
        return redirect(next_url)
    else:
        return redirect('main_app:index')

def show_my_gifts(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request,'accounts/my_gifts.html',{'user_gifts':user.gifts.all()})
    else:
        return redirect('accounts_app:login')
from apps.message.models import Message
def show_my_messages(request):
    if request.user.is_authenticated:
         
        mobile_number = request.user.mobile_number
        user_messages = Message.objects.filter(mobile_number=mobile_number)
        return render(request,'accounts/my_messages.html',{'user_messages':user_messages})
    else:
        return redirect('accounts_app:login')
    
def show_my_transactions(request):
    try:
        customer = Customer.objects.get(phone_number=request.user.mobile_number)
    except ObjectDoesNotExist:
        error(request,_("مشتری پیدا نشد."),"error")
        return redirect("accounts_app:user_panel")
    except:
        error(request,_("خطا در اجرای عمللیات!"),"error")
        return redirect("accounts_app:user_panel")
        
    payments = Payment.objects.filter(customer=customer)
    return render(request,"accounts/my_transactions.html",{"payments":payments})


def change_profile_and_full_name(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request,"accounts/partials/change_profile_and_fullname.html",{})
        else:
            error(request,_('شما ابتدا باید وارد شوید.'),'error')
            return redirect('accounts_app:login')
    else:
        try:
            user = request.user
            user.name = request.POST.get('name')
            user.family = request.POST.get('last_name')
            if user.profile != "images/account/profile/NaN.png":
                path = settings.MEDIA_ROOT+str(user.profile)
                if isfile(path):
                    remove(path)
            try:
                user.profile = request.FILES['profile']
            except:
                pass
            user.save()
        except ObjectDoesNotExist:
            error(request,_("کاربر پیدا نشد"),"error")
            return redirect("accounts_app:user_panel")
        except:
            error(request,_("خطا در اجرای عملیات!"),"error")
            return redirect("accounts_app:user_panel")
        success(request,_("با موفقیت اطلاعات تغییر کرد."),"success")
        return redirect("accounts_app:user_panel")
    
def save_location(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user=request.user
            user.latitude_location = request.POST.get("latitude_location")
            user.longitude_location = request.POST.get("longitude_location")
            user.save()
            return HttpResponse("ذخیره شد.")