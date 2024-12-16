# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django import forms
# from .models import CustomUser
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
class MukbangForm(forms.Form):
    description = forms.CharField(label=_("توضیحات"), widget=forms.TextInput(attrs={'class' : 'input','placeholder':_('توضیحات را وارد کنید.'),'title':_('لطفا توضیحات را وارد کنید.')}))
    video = forms.FileField(label=_("ویدئو"), widget=forms.FileInput(attrs={'class' : 'input','placeholder':_('ویدئوی مورد نظر را آپلود کنید.'),'title':_('لطفا ویدئوی مورد نظر را آپلود کنید')}))
    poster = forms.FileField(label=_("پوستر"), widget=forms.FileInput(attrs={'class' : 'input','placeholder':_('پوستر مورد نظر را آپلود کنید.'),'title':_('لطفا پوستر مورد نظر را آپلود کنید')}))