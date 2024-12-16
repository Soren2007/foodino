from django.shortcuts import render,redirect
from .models import Email
from apps.accounts.models import CustomUser
from datetime import datetime
from utils import send_mail
from django.conf import settings
from django.contrib.messages import error,success
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import error,success
# Create your views here.


def send_emails(request):
    if request.user.is_authenticated and request.user.is_admin:
        sended_emails_number = 0
        email_objects = Email.objects.filter(is_active=True,register_date_time__gt = datetime.now)
        for email_object in email_objects:
            if email_object.mod == "1":
                emails = (object.email for object in CustomUser.objects.all())
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
                    
            elif email_object.mod == "2":
                emails = (object.email for object in email_object.users.all())
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
                    
            elif email_object.mod == "3":
                emails = (object.email for object in CustomUser.objects.filter(country__in = email_object.country.all()))
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
                    
            elif email_object.mod == "4":
                emails = (object.email for object in CustomUser.objects.filter(is_admin = True))
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
                    
            elif email_object.mod == "5":
                emails = (object.email for object in CustomUser.objects.filter(is_support = True))
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
                    
            elif email_object.mod == "6":
                emails = (object.email for object in CustomUser.objects.filter(is_serviceman = True))
                if len(emails) > 0:
                    send_mail(email_object.subject, email_object.message,settings.EMAIL,emails)
                    sended_emails_number+=1
            else:
                error(request,_("مد ارسال شده پیدا نشد."),"error")
                return redirect()
        success(request,"","success")
        return redirect()
    error(request,_("شما نمیتوانید وارد این صفحه شوید!"),"error")
    return redirect("main_app:index")  