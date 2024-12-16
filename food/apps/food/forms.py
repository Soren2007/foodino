# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django import forms
class Food_Stuff_Form(forms.Form):
    stuff_name = forms.CharField(label="نام ماده")
    stuff_price = forms.IntegerField(label="قیمت ماده به تومان")
    
class Food_Group_Form(forms.Form):
    group_name = forms.CharField(label="نام دسته")
    
# class Food_Form(forms.Form):
#     food_name = forms.CharField(label="نام غذا")
#     food_image = forms.ImageField(label="تصویر غذا")
    
    
    
    #     food_name = models.CharField(max_length=60,verbose_name="نام غذا")
    # food_image = models.ImageField(upload_to=f"images/foods/",verbose_name="تصویر غذا")
    # food_stuffs = models.ManyToManyField(Stuff,verbose_name="مواد استفاده شده")
    # food_price  = models.CharField(max_length=7, verbose_name="قیمت غذا")
    # food_dastor = models.TextField(verbose_name="دستور پخت")
    # food_time = models.TimeField(verbose_name="زمان پخت غذا")
    # food_wight = models.CharField(max_length=10,verbose_name="وزن غذا")
    # food_kalery = models.CharField(max_length=10,verbose_name="کالری غذا")
    # food_group = models.ForeignKey(Group,verbose_name="دسته‌بندی",on_delete=models.CASCADE)
    # register_date = models.DateTimeField(auto_now_add=True,verbose_name="register date")