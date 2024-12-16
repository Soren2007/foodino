from django.shortcuts import render
from .models import wheel_of_luck,Lottery
from apps.accounts.models import CustomUser
from random import choice,randint
from utils import send_sms
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
# Create your views here.

def show_wheel_of_luck(request):
    wheel_of_lucks = wheel_of_luck.objects.all()
    return render(request, "gift/wheel_of_luck.html", {"wheel_of_lucks":wheel_of_lucks})

def get_gift_in_wheel_of_luck(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            wheel_of_luck_object = wheel_of_luck.objects.get(id=request.POST.get("wheel_of_luck_id"))
            gifts = wheel_of_luck_object.gifts.all()
            gifts_len = len(gifts)
            index = randint(0, (gifts_len-1))
            try:
                request.session['user_session']['mobile_number']
            except:
                pass
            user = CustomUser.objects.get(mobile_number=request.session['user_session']['mobile_number'])
            user_gifts=list(user.gifts.all())
            user_gifts.append(gifts[index])
            user.gifts.set(list(set(user_gifts)))
            user.save()
            deg = ((360/gifts_len * (index+1))+30) * -1
            return HttpResponse(deg) 
        else:
            return HttpResponse("Error")
        

def show_lotteries(request):
    lotteries=Lottery.objects.filter(is_active=True)
    users_length = len(CustomUser.objects.all())
    return render(request, "gift/show_lotteries.html", {"lotteries":lotteries})
def wins_lottery(request):
    if request.method == "POST":
        lottery_id = request.POST.get("lottery_id")
        try:
            lottery=Lottery.objects.get(id=lottery_id)
        except:
            pass
        if request.POST.get('is_end') == "false":
            users = list(CustomUser.objects.all())
            index = randint(0, len(users)-1)
            user = users[index]
            message = f"سایت فودینو\nدرود شما در قرعه‌کشی {lottery.title} برنده شده اید شما در قسمت هدایا می توانید از هدیه خود استفاده کنید."
            send_sms(request,user.mobile_number,message)
            user_gifts=list(user.gifts.all())
            user_gifts+list(lottery.gifts.all())
            user.gifts.set(user_gifts)
            user.save()
            return HttpResponse(index)
        else:
            lottery.is_done =True
            lottery.is_start = False
            lottery.save()
            return HttpResponse("ok")