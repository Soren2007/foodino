# File version
__version__ = "1.1.1"
# File Description
"""
this python file
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
"""
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from apps.message.models import UserChatRoom
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
import openai
openai.api_key = "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"
models = openai.Model.list()
# create a chat completion
def open_ai_chat_gpt(request):
    if request.method == "POST":
        message = request.POST.get("message")
        phone_number = request.POST.get("phone_number")
        try:
            user = UserChatRoom.objects.get(phone_number=phone_number)
        except:
            return redirect('main_app:index')
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
        answer = chat_completion.choices[0].message.content
        ChatGPT.objects.create(message=message,answer=answer,user=user).save()
        return HttpResponse(answer)