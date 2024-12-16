# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from apps.accounts.models import CustomUser
from .models import Mukbang
from .forms import MukbangForm
from django.views import View
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.messages import success,error
from django.utils.translation import gettext_lazy as _
# Create your views here.

class AddMukbangView(View):
    def get(self, request, *args,**kwargs):
        form = MukbangForm()
        return render(request, 'mukbang/add_mukbang.html',{'form':form})
    def post(self, request, *args, **kwargs):
        user = request.user
        mukbang = Mukbang()
        mukbang.user = user
        mukbang.video = request.FILES['video']
        mukbang.poster_image = request.FILES['poster']
        mukbang.description = request.POST.get('description')
        mukbang.save()
        success(request,_('با موفقیت ذخیره شد.'),'success')
        return render(request, 'mukbang/add_mukbang.html')
def show_info(request):
    if request.method == "POST":
        mukbang_id = request.POST.get("mukbang_id")
        mukbang = Mukbang.objects.get(id=mukbang_id)
        return render(request, "mukbang/mukbang_info_box.html",{"mukbang":mukbang})