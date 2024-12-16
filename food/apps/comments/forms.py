# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django import forms
from django.utils.translation import gettext_lazy as _
class CommentForm(forms.Form):
    food_id = forms.CharField(widget=forms.HiddenInput(),required=False)
    comment_id = forms.CharField(widget=forms.HiddenInput(),required=False)
    comment_text = forms.CharField(label="",error_messages={'required':_('این فیلد نمی تواند خالی باشد!')},widget=forms.Textarea(attrs={'class':'input textarea-input','placeholder':_('متن نظر را وارد کنید.'),'title':_('لطفا متن نظر را وارد کنید.'),'rows':'4'}))