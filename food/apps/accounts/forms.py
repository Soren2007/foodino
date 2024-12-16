from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    re_password = forms.CharField(label='RePassword',widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['mobile_number']
    def clean_re_password(self):
        password=self.cleaned_data['password']
        re_password=self.cleaned_data['re_password']
        if password and re_password and password != re_password:
            raise ValidationError(_('رمز عبور و تکرار آن باهم مغایرت دارند'))
        return re_password
    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# class CompileInformationForm(forms.ModelForm):

# # class CompileInformationForm(forms.Form):
#     name = forms.CharField(label='نام',widget=forms.TextInput(attrs={'class' : 'input','placeholder':'نام خود را وارد کنید.','title':' لطفا نام خود را وارد کنید.'}))
#     family = forms.CharField(label='نام خانوادگی',widget=forms.TextInput(attrs={'class' : 'input','placeholder':'نام خانوادگی خود را وارد کنید.','title':' لطفا نام خانوادگی خود را وارد کنید.'}))
#     email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={'class' : 'input','placeholder':'ایمیل خود را وارد کنید.','title':' لطفا ایمیل خود را وارد کنید.'}))
#     address = forms.EmailField(label='آدرس',widget=forms.Textarea(attrs={'class' : 'input','placeholder':'آدرس خود را وارد کنید.','title':' لطفا آدرس خود را وارد کنید.'}))
#     birth_date = forms.DateField(label='تاریخ تولد',widget=forms.DateInput(attrs={'class' : 'input','placeholder':'تاریخ تولد خود را وارد کنید.','title':' لطفا تاریخ تولد خود را وارد کنید.','type':'date'}))
#     national_code = forms.CharField(label='کدملی',widget=forms.TextInput(attrs={'class' : 'input','placeholder':'کدملی خود را وارد کنید.','title':' لطفا کدملی خود را وارد کنید.'}))
#     # gender = forms.EmailField(label='جنسیت',widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':'جنسیت خود را وارد کنید.','title':' لطفا جنسیت خود را وارد کنید.'}))
    
#     class Meta:
#         model = CustomUser
#         fields = ('name','family','email','address','birth_date','national_code','gender')
        
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField(help_text=_("برای تغییر رمز عبور روی این <a href='../password'>لینک</a> کلیک کنید."))
    class Meta:
        model = CustomUser
        fields = ['mobile_number','email','name','family','password','gender','is_active','is_admin']
class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label=_('رمز عبور'),widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':_('رمز عبور را وارد کنید.'),'title':_(' لطفا رمز عبور را وارد کنید.'),'autocomplete':'off'}))
    re_password = forms.CharField(label=_('تکرار رمز عبور'),widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':_('تکرار رمز عبور را وارد کنید.'),'title':_(' لطفا تکرار رمز عبور را وارد کنید.'),'autocomplete':'off'}))
    class Meta:
        model = CustomUser
        fields = ('mobile_number','password',)
        widgets ={'mobile_number': forms.NumberInput(attrs={'class' : 'input','placeholder':'شماره موبایل خود را وارد کنید.','title':'لطفا شماره موبایل خود را وارد کنید.'})}
    def clean_re_password(self):
        password=self.cleaned_data['password']
        re_password=self.cleaned_data['re_password']
        if password and re_password and password != re_password:
            raise ValidationError(_('رمز عبور و تکرار آن باهم مغابرت دارند'))
        return re_password

class VerifyRegisterCodeForm(forms.Form):
    active_code = forms.CharField(label=_("کد فعال سازی"), error_messages={'required':_('این فیلد نمی تواند خالی باشد.')}, widget=forms.TextInput(attrs={'class' : 'input','placeholder':_('کد دریافتی را وارد کنید.'),'title':_('لطفا کد دریافتی را وارد کنید.'),'autocomplete':'off'}))

class LoginUserForm(forms.Form):
    mobile_number = forms.CharField(label=_("شماره موبایل"), error_messages={'required':_('این فیلد نمی تواند خالی باشد.')}, widget=forms.NumberInput(attrs={'class' : 'input','placeholder':_('شماره موبایل  خود را وارد کنید.'),'title':_('لطفا شماره موبایل خود را وارد کنید.'),'maxlength':'11','autocomplete':'off'}))
    password = forms.CharField(label=_("رمز عبور"), error_messages={'required':_('این فیلد نمی تواند خالی باشد.')}, widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':_('رمز عبور خود را وارد کنید.'),'title':_('لطفا رمز عبور خود را وارد کنید.'),'autocomplete':'off'}))
class ChangePasswordForm(forms.Form):
    password = forms.CharField(label=_('رمز عبور'),widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':_('رمز عبور را وارد کنید.'),'title':_(' لطفا رمز عبور را وارد کنید.'),'autocomplete':'off'}))
    re_password = forms.CharField(label=_('تکرار رمز عبور'),widget=forms.PasswordInput(attrs={'class' : 'input','placeholder':_('تکرار رمز عبور را وارد کنید.'),'title':_(' لطفا تکرار رمز عبور را وارد کنید.'),'autocomplete':'off'}))
    def clean_re_password(self):
        password=self.cleaned_data['password']
        re_password=self.cleaned_data['re_password']
        if password and re_password and password != re_password:
            raise ValidationError(_('رمز عبور و تکرار آن باهم مغابرت دارند'))
        return re_password
class RememberPasswordForm(forms.Form):
    mobile_number = forms.CharField(label="", error_messages={'required':_('این فیلد نمی تواند خالی باشد.')}, widget=forms.NumberInput(attrs={'class' : 'input','placeholder':_('شماره موبایل  خود را وارد کنید.'),'title':_('لطفا شماره موبایل خود را وارد کنید.')}))
    