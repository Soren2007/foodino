# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from .models import *
from django.contrib.messages import success,error
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def show_box(request):
    try:
        chat_session=request.session['chat_session']
    except:
        return render(request,'partials/chat_box.html')

    return render(request,'partials/chat_box.html',{'chat_session':chat_session})

def add_message(request):
    if request.method == "POST":
        message = Message()
        message.name = request.POST['name']
        message.family = request.POST['family']
        message.email = request.POST['email']
        message.mobile_number = request.POST['mobile_number']
        message.subject = request.POST['subject']
        message.message = request.POST['message']
        message.save()
        success(request,_('پیام شما با موفقیت ارسال شد.'),'success')
        return redirect('main_app:index')
    return render(request,"message/contact_us/show.html")
def add_user_in_chat_room(request):
    if request.method == "POST" and not str(request.POST.get('full_name')) == "":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        avatar = request.POST.get('avatar')
        user=UserChatRoom.objects.filter(phone_number=phone_number)
        is_exists=user.exists()
        chat_info_dict = {'is_exist': True,'full_name': full_name,'phone_number': phone_number,'avatar':avatar,'messages_len':0}
        request.session['chat_session']=chat_info_dict
        if is_exists:
            user.update(full_name=full_name,phone_number=phone_number,is_exist=True,avatar=avatar)
        else:
            UserChatRoom.objects.create(full_name=full_name,phone_number=phone_number,is_exist=True,avatar=avatar)
        return redirect('message_app:show_chat')
    return render(request,"message/chat/partials/chatroom_add_user_form.html")
def add_message_online_chat(request):
    message=request.GET.get('message')
    try:
        user=UserChatRoom.objects.get(phone_number=request.session['chat_session']['phone_number'])
    except:
        return redirect("main_app:index")
    ChatRoom.objects.create(message_text=message,sender_user=user)
    return redirect("message_app:show_messages")

def show_messages(request):
    is_manage_chat = request.GET.get("is_manage_chat")
    print(100*'-')
    print(is_manage_chat)
    print(100*'-')
    if is_manage_chat == 'true':
        try:
            user = UserChatRoom.objects.get(phone_number=request.GET.get('phone_number'))
            # request.session['chat_session']['messages_len'] = len(user.message_user.all())
        except:
            print('error')
            # return redirect("main_app:index")
        return render(request,'message/chat/partials/chat_body.html',{'user_object':user,'is_manage_chat':is_manage_chat})    
    try:
        user = UserChatRoom.objects.filter(phone_number=request.session['chat_session']['phone_number'])[0]
        # request.session['chat_session']['messages_len'] = len(user.message_user.all())
        return render(request,'message/chat/partials/chat_body.html',{'user_object':user ,'is_manage_chat':is_manage_chat})    
    except:
        return redirect("message_app:start_online_chat")
        # <input type="hidden" value="" name="parent_id" id="id_parent_id">
        # <input type="hidden" value="{{user_object.phone_number}}" name="user_phone_number_input_hidden" id="id_user_phone_number_input_hidden">
def refresh_messages (request):
    if request.method == "POST":    
        user = UserChatRoom.objects.get(phone_number=request.POST.get('phone_number'))
        is_manage_chat = request.POST.get("is_manage_chat")
        length = len(user.message_user.all())
        print(100*'-')
        print(user)
        print(length)
        print(100*'-')
        if is_manage_chat == "true":
            request.session['chat_session']['messages_len'] = len(user.message_user.all())
            return render(request,'message/chat/partials/refresh_messages_manager.html',{'user_object':user ,'is_manage_chat':is_manage_chat})
        else:
            request.session['chat_session']['messages_len'] = len(user.message_user.all())
            return render(request,'message/chat/partials/refresh_messages_user.html',{'user_object':user,'is_manage_chat':'false' })
            
        # return HttpResponse("false")

def show_chat_room(request):
    return render(request,"message/chat/partials/show_chatroom.html",{'online_chat_data':request.session['chat_session']})

def clear_chat(request):
    try:
        ChatRoom.objects.get(sender_user=UserChatRoom.objects.get(phone_number=request.session['chat_session']['phone_number'])).delete()
        # request.session['chat_session'] = {}
    except:
        error(request,_("خطا در اجرای عملیات"),"error")
        return redirect('main_app:index')
    return redirect('message_app:show_messages')
def manage_chat_room(request):
    if request.user.is_support:
        try:
            user = UserChatRoom.objects.filter(phone_number=request.user.mobile_number)[0]
        except ObjectDoesNotExist:
            error(request,_("پشتیبان یافت نشد"), "error")
            return redirect('main_app:index') 
        else:
            if user.is_support:
                user_chat_rooms=UserChatRoom.objects.all()
                return render(request,'message/chat/manage_chat_room.html',{'user_chat_rooms':user_chat_rooms})
            else:
                error(request,_('شما اجازه ورود ندارید.'), 'error')
                return redirect('main_app:index')
    error(request,_('شما اجازه ورود ندارید.'), 'error')
    return redirect('main_app:index')

def show_messages_in_manage_chat_room(request):    
    phone_number = request.user.mobile_number
    try:
        user = UserChatRoom.objects.filter(phone_number=phone_number)[0]
    except:
        error(request,_("شما مجوز ورود به پنل مدیریت پیام‌ها را ندارید!"), "error")
        return redirect('message_app:show_messages_in_manage_chat_room')
    else:
        model=request.GET.get('model')
        parent_id=request.GET.get('parent_id')
        if model == 'send_message':
            if parent_id:
                ChatRoom.objects.create(
                    sender_user=user,
                    receiver_user=UserChatRoom.objects.get(phone_number=request.GET.get('receiver_user_phone_number')),
                    message_text=request.GET['message'],
                    message_parent = ChatRoom.objects.filter(id=request.GET['parent_id'])[0]
                    )
            else: 
                ChatRoom.objects.create(
                    sender_user=user,
                    receiver_user=UserChatRoom.objects.get(phone_number=request.GET.get('receiver_user_phone_number')),
                    message_text=request.GET['message'],
                    )   
            return render(request,'message/chat/partials/chat_body.html',{'user_object':user,'is_manage_chat':'true' ,'model':model})
        return render(request,'message/chat/partials/chat_body.html',{'user_object':user,'is_manage_chat':'true' })
