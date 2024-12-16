# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from django.conf import settings
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.orders.models import Order
from apps.reservation.models import Reservation
from requests import post
from json import dumps
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import success,error,warning
from .models import Payment
from apps.accounts.models import Customer
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
MERCHANT = '1344b5d4-0048-11e8-94db-005056a205be'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
CallbackURL = 'http://127.0.0.1:8080/payment/verify/'
class ZarinpalPaymentView(LoginRequiredMixin,View):
    def get(self, request,order_id):
        try:
            order=Order.objects.get(id=order_id)
            description= order.description 
            user=request.user
            if order:
                payment = Payment.objects.create(
                    order = order,
                    customer = Customer.objects.get(user=user),
                    amount = order.get_order_total_price(),
                    description=description
                )
            else:
                payment = Payment.objects.create(
                    customer = Customer.objects.get(user=user),
                    amount = order.get_order_total_price(),
                    description=description
                )
                
            payment.save()
            request.session['payment_session']={'order_id':order_id,'payment_id':payment.id}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.get_order_total_price(),
                "callback_url": CallbackURL,
                "description": description,
                "metadata":{'mobile':user.mobile_number,'email':user.email,},
            }
            req_header = {"accept": "application/json", "content-type": "application/json'"}
            req = post(url=ZP_API_REQUEST, data=dumps(req_data),headers=req_header)
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) ==0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f'Error code: {e_code}, Error Message: {e_message}')
        except ObjectDoesNotExist:
            error(request,_('فاکتوری با این مشخصات پیدا نشد.'),'error')
            return redirect('orders_app:check_out_order',order_id)
        except:
            error(request,_('خطا در انتقال به درگاه بانکی زرین پال!'),'error')
            return redirect('orders_app:check_out_order',order_id)
class ZarinpalPaymentVerifyView(LoginRequiredMixin,View):
    def post(self,request):
        print(1000*"-")
    def get(self,request):
        order_id=request.session['payment_session']['order_id']
        payment_id=request.session['payment_session']['payment_id']
        order=Order.objects.get(id=order_id)
        payment=Payment.objects.get(id=payment_id)
        t_authority = request.GET.get('Authority')
        if request.GET.get('Status') == 'OK':
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.get_order_total_price(),
            }
            req_header = {'accept': "application/json", "content-type": "application/json'"}
            req = post(url=ZP_API_VERIFY,data=dumps(req_data),headers=req_header)
            t_status = req.json()['errors']['code']
            if len(req.json()['errors']) >= 0:
                if t_status ==100:
                    self.request.session['food_data_cart'] = {}
                    self.request.session['my_recipes_data_cart'] = {}
                    order.is_finally = True
                    order.save()
                    payment.is_finally = True
                    payment.status_code = t_status
                    payment.ref_id = str(req.json()['data']['ref_id'])
                    payment.save()
                    return redirect('payment_app:show_verify_message',f"پرداخت با موفقیت انجام شد، کد رهگیری شما : {str(req.json()['data']['ref_id'])}")
                elif t_status ==101:
                    self.request.session['food_data_cart'] = {}
                    self.request.session['my_recipes_data_cart'] = {}
                    order.is_finally = True
                    order.save()
                    payment.is_finally = True
                    payment.status_code = t_status
                    payment.ref_id = str(req.json()['data']['ref_id'])
                    payment.save()
                    return redirect('payment_app:show_verify_message',f"پرداخت با موفقیت انجام شد، کد رهگیری شما : {str(req.json()['data']['ref_id'])}")
                else:
                    payment.status_code = t_status
                    payment.save()
                    return redirect('payment_app:show_verify_message',f"پرداخت قبلا انجام شد، کد رهگیری شما : {str(req.json()['data']['ref_id'])}")
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return redirect('payment_app:show_verify_message',f"خطا در فرایند پرداخت، کد خطا: {e_code}")
        else:
            return redirect('payment_app:show_verify_message',"خطا در فرایند پرداخت!")
def show_verify_message(request,message):
    return render(request,'payment/verify_message.html',{'message':message})