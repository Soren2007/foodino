# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,get_object_or_404,redirect
from .food_cart import *
from django.views import View
from apps.food.models import Food,MyRecipes
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.accounts.models import Customer,Country,City
from apps.branch.models import Branch
from .models import Order,OrderDetails,PaymentType,OrderStatus,OrderDetailsSubscription
from apps.subscription.models import Subscription
from apps.discounts.models import Coupon
from apps.delivery.models import Delivery
from django.db.models import Q
from datetime import datetime
from django.contrib.messages import success,error,warning
from django.core.exceptions import ObjectDoesNotExist
from utils import price_by_delivery_tax
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

# @csrf_protect
class CartsView(View):
    def get(self,request,*args, **kwargs):
        food_cart = FoodCart(request)
        my_recipe_cart = MyRecipeCart(request)
        return render(request, 'orders/show.html',{'food_cart':food_cart,'my_recipe_cart':my_recipe_cart})

def show_carts(request):
    my_recipe_cart = MyRecipeCart(request)
    food_carts = FoodCart(request)
    total_price = food_carts.calc_total_price() + my_recipe_cart.calc_total_price()
    order_final_price,delivery,tax=price_by_delivery_tax(total_price)
    return render(request, 'orders/partials/show_carts.html',{'food_carts':food_carts,'my_recipe_cart':my_recipe_cart,'total_price':total_price,'delivery':delivery,'tax':tax,'order_final_price':order_final_price})
from .models import how_to_use
def show_how_to_use(request):
    how_to_uses = how_to_use
    return render(request, "orders/partials/set_how_to_use.html",{"how_to_uses":how_to_uses})

def add_to_food_cart(request):
    if request.method == "POST":
        food_id=request.POST.get('food_id')
        how_to_use=request.POST.get('how_to_use')
        qty=request.POST.get('qty')
        food_cart = FoodCart(request)
        food=get_object_or_404(Food,id=food_id)
        food_cart.add_to_food_cart(food,qty,how_to_use)
        return redirect('orders_app:show_carts') 
        


def add_to_my_recipe_cart(request):
    if request.method == "POST":
        my_recipe_id=request.POST.get('my_recipe_id')
        how_to_use=request.POST.get('how_to_use')
        qty=request.POST.get('qty')
        my_recipe_cart = MyRecipeCart(request)
        my_recipe=get_object_or_404(MyRecipes,id=my_recipe_id)
        my_recipe_cart.add_to_my_recipe_cart(my_recipe,qty,how_to_use)
        return redirect('orders_app:show_carts')

def update_from_food_cart(request):
    if request.method == "POST":
        food_id=request.POST.get('food_id')
        qty=request.POST.get('qty')
        food_cart = FoodCart(request)
        food=get_object_or_404(Food,id=food_id)
        food_cart.update_from_food_cart(food,qty)
        return redirect('orders_app:show_carts')

def update_from_my_recipe_cart(request):
    if request.method == "POST":
        my_recipe_id=request.POST.get('my_recipe_id')
        qty=request.POST.get('qty')
        my_recipe_cart = MyRecipeCart(request)
        my_recipe=get_object_or_404(MyRecipes,id=my_recipe_id)
        my_recipe_cart.update_from_my_recipe_cart(my_recipe,qty)
        return redirect('orders_app:show_carts')

def delete_form_food_cart(request):
    if request.method == "POST":
        food_id=request.POST.get('food_id')
        food_cart = FoodCart(request)
        food=get_object_or_404(Food,id=food_id)
        food_cart.delete_from_food_cart(food)
        return redirect('orders_app:show_carts')

def delete_form_my_recipe_cart(request):
    if request.method == "POST":
        my_recipe_id=request.POST.get('my_recipe_id')
        my_recipe_cart = MyRecipeCart(request)
        my_recipe=get_object_or_404(MyRecipes,id=my_recipe_id)
        my_recipe_cart.delete_from_my_recipe_cart(my_recipe)
        return redirect('orders_app:show_carts')

def status_of_carts(request):
    if request.method == "POST":
        food_cart  = FoodCart(request)
        my_recipe_cart  = MyRecipeCart(request)
        return HttpResponse(food_cart.food_count+my_recipe_cart.my_recipes_count)

# def CreateOrderView(request):
from django.conf import settings
from utils import QR
class CreateFoodOrderView(LoginRequiredMixin,View):
    def get(self, request):
        try:
            customer = get_object_or_404(Customer,user=request.user)
        except:
            customer=Customer.objects.create(user=request.user)
        # except:
        #     error(request,"خطا درانجام عملیات!","error")
        #     return redirect("orders_app:carts")
        try:
            order = Order.objects.create(customer=customer,payment=get_object_or_404(PaymentType,id=1),status = get_object_or_404(OrderStatus,id=1))
            qr_path = f"{settings.BASE_DIR}/media/images/order/qr_code/"
            if QR(order.order_code,order.qr_code_color,11,qr_path,order.order_code,'jpg').create_qr() == "ok":
                order.qr_code_image = f"images/order/qr_code/{order.order_code}.jpg"
            order.save()
        except ObjectDoesNotExist:
            error(request,_('نوع پرداخت وجود ندارد.'))
            return redirect("orders_app:carts")
        # except:
        #     error(request,_("خطا درانجام عملیات!"),"error")
        #     return redirect("orders_app:carts")
        
        food_cart = FoodCart(request)
        for item in food_cart: 
            food = Food.objects.get(id=item['food']['id'])
            OrderDetails.objects.create(order=order,food=food,price=item['price'],qty=item['qty'],how_to_use=item['how_to_use']).save()
        my_recipe_cart = MyRecipeCart(request)
        for item in my_recipe_cart:
            OrderDetails.objects.create(order=order,my_recipes=item['my_recipe'],price=item['price'],qty=item['qty'],how_to_use=item['how_to_use']).save()
        return redirect('orders_app:check_out_order',order.id)
    
class CreateSubscriptionOrderView(LoginRequiredMixin,View):
    def get(self, request):
        try:
            customer = get_object_or_404(Customer,user=request.user)
        except:
            customer=Customer.objects.create(user=request.user)
        # except:
        #     error(request,"خطا درانجام عملیات!","error")
        #     return redirect("orders_app:carts")
        try:
            order = Order.objects.create(customer=customer,payment=get_object_or_404(PaymentType,id=1),status = get_object_or_404(OrderStatus,id=1))
            qr_path = f"{settings.BASE_DIR}/media/images/order/qr_code/"
            if QR(order.order_code,order.qr_code_color,11,qr_path,order.order_code,'jpg').create_qr() == "ok":
                order.qr_code_image = f"images/order/qr_code/{order.order_code}.jpg"
            order.save()
        except ObjectDoesNotExist:
            error(request,_('نوع پرداخت وجود ندارد.'))
            return redirect("orders_app:carts")
        except:
            error(request,_("خطا درانجام عملیات!"),"error")
            return redirect("orders_app:carts")
        
        try:
            subscription=Subscription.objects.get(id)
        except ObjectDoesNotExist:
            return redirect("")
        except:
            error(request,_("خطا درانجام عملیات!"),"error")
            return redirect("orders_app:carts")
        
        OrderDetailsSubscription.objects.create(order=order,subscription=subscription).save()
        return redirect('orders_app:check_out_order',order.id)
    
    
    
    
     
    
    
def show_cities_with_country(request):
    if request.method == "POST":
        cities =  City.objects.filter(country = request.POST.get("country_id"))
        return render(request,"orders/partials/show_cities.html",{"cities":cities}) 
def find_branch(request):
    if request.method == "POST":
        branches=Branch.objects.filter(branch_city=request.POST.get('city_id'),is_active=True)
        return render(request,"orders/partials/show_branches.html",{'branches':branches})
class CheckOutOrderView(LoginRequiredMixin,View):
    def get(self, request, order_id):
        payments=PaymentType.objects.all()
        user = request.user
        customer = get_object_or_404(Customer,user=user)
        food_cart = FoodCart(request)
        my_recipe_cart = MyRecipeCart(request)
        order = get_object_or_404(Order,id=order_id)
        total_price = food_cart.calc_total_price() + my_recipe_cart.calc_total_price()
        order_final_price,delivery,tax=price_by_delivery_tax(total_price,order.discount)
        countries = Country.objects.all()
        data = {
            'name':user.name,
            'family':user.family,
            'email':user.email,
            'phone_number':customer.phone_number,
            'address':customer.address,
            'description':order.description,
            'payment':order.payment,
            'order_id':int(order_id),
            # customer.country
            'country_id':""
        }
        return render(request, 'orders/checkout.html',{'food_cart':food_cart,'my_recipe_cart':my_recipe_cart,'total_price':total_price,'delivery':delivery,'order_final_price':order_final_price,'tax':tax,'payments':payments,'data':data,'countries':countries})
    def post(self, request,order_id):
        try:
            try:
                branch = Branch.objects.get(id=request.POST.get('branch'))
            except ObjectDoesNotExist:
                error(request,_("شعبه مورد نظر یافت نشد."))
                return redirect('orders_app:check_out_order',order_id)
            delivery=Delivery.objects.filter(branch=branch).order_by('-your_last_activity')
            order=Order.objects.get(id=order_id)
            order.delivery = delivery[0]
            order.description = request.POST.get('description')
            order.payment = PaymentType.objects.get(id=request.POST.get('payment'))
            order.save()
            user = request.user
            user.name = request.POST.get('name')
            user.family = request.POST.get('family')
            user.email = request.POST.get('email')
            user.save()    
            customer=Customer.objects.get(user=user)
            customer.phone_number=request.POST.get('phone_number')
            customer.country=Country.objects.get(id=request.POST.get('country'))
            customer.city=City.objects.get(id=request.POST.get('city'))
            customer.address=request.POST.get('address')
            customer.save()
            success(request,'اطلاعات با موفقیت ثبت شد.','success')
            # return redirect('orders_app:check_out_order',order_id)
            return redirect('payments_app:zarinpal_payment',order_id)
        except ObjectDoesNotExist:
            error(request,_('فاکتوری با این مشخصات پیدا نشد.'),'error')
            return redirect('orders_app:check_out_order',order_id)
        # except:
        #     error(request,_('خطا در انجام عملیات!'),'error')
        #     return redirect('orders_app:check_out_order',order_id)

def apply_coupon(request):
    if request.method == "POST":
        order_id= request.POST.get('order_id')
        coupon_code = request.POST.get('coupon_code')
        coupon = Coupon.objects.filter(Q(coupon_code=coupon_code)&Q(is_active=True)&Q(start_date__lte=datetime.now()) & Q(end_date__gte=datetime.now()))
        discount = 0
        try:
            order=Order.objects.get(id=order_id)
            if coupon:
                discount = coupon[0].discount
                order.discount=discount
                order.save()
                success(request,_('اعمال کوپن با موفقیت انجام شد.'),'success')
            else:
                order.discount=discount
                order.save()
                error(request,_('کد وارد شده معتبر نیست.'),'error')
        except:
            error(request,_('کد وارد شده معتبر نیست.'),'error')
        return redirect('orders_app:check_out_order',order_id)

def show_my_orders(request):
    user = request.user
    try:
        orders = Order.objects.filter(customer=Customer.objects.get(user=user))
    except:
        error(request,_('کاربر یافت نشد.'),'error')
        return redirect("main_app")
    page_object_number = 12
    paginator=Paginator(orders,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'orders/my_orders.html',{"page_obj":page_obj,'obj_len':len(orders),'page_object_number':page_object_number})


def show_my_order_details(request):
    user = request.user
    try:
        orders = Order.objects.filter(customer=Customer.objects.get(user=user))
    except:
        error(request,_('کاربر یافت نشد.'),'error')
        return redirect("main_app")
    page_object_number = 12
    paginator=Paginator(orders,page_object_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'orders/my_orders.html',{"page_obj":page_obj,'obj_len':len(orders),'page_object_number':page_object_number})



def orders_panel(request):
    orders = Order.objects.filter(is_finally = True)
    statuses=Order.status_list
    return render(request, "orders/orders_panel.html", {"orders":orders,"statuses":statuses})

def order_details_panel(request,order_id):
    order = Order.objects.get(id=order_id)
    order_details=OrderDetails.objects.filter(order=order)
    return render(request, "orders/order_detail_panel.html", {"order_details":order_details})

def change_status_order(request):
    if request.method == "POST":
        try:
            order = Order.objects.get(id=request.GET.get("order_id"))
            order.status = request.GET.get("status_id")
            order.save()
        except ObjectDoesNotExist:
            error(request,_("سفارش پیدا نشد."),"error")
        return HttpResponse("ok")