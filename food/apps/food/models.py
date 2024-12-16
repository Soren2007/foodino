# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from django.utils import timezone
from Middleware.middleware import RequestMiddleware
from apps.accounts.models import CustomUser
from apps.blog.models import KeyWord
from django.utils.translation import gettext_lazy as _
# from ckeditor.fields import RichTextField
# Create your models here.
class FoodGroup(models.Model):
    class_name = "FoodGroup"
    group_name = models.CharField(max_length=50,verbose_name=_("نام دسته"))
    group_image = models.ImageField(upload_to="images/food/food_group/", verbose_name=_("تصویر گروه"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    
    def fields_information(self):
        return [{"field_name":"group_name","verbose_name":'نام دسته',"value":self.group_name},{"field_name":"group_image","verbose_name":"تصویر دسته","value":self.group_image}]
    def __str__(self):
        return f"{self.group_name}"
    class Meta:
        verbose_name = _("دسته‌بندی غذا")
        verbose_name_plural = _("دسته‌بندی‌های غذا")
        db_table ="table_food_group"
class StuffGroup(models.Model):
    class_name = "StuffGroup"
    group_name = models.CharField(max_length=50,verbose_name=_("نام دسته"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"group_name","verbose_name":'نام دسته',"value":self.group_name}]
    def __str__(self):
        return f"{self.group_name}"
    class Meta:
        verbose_name = _("دسته‌بندی مواد")
        verbose_name_plural = _("دسته‌بندی‌های مواد")
        db_table ="table_stuff_group"
class Stuff(models.Model):
    class_name = "Stuff"
    stuff_name = models.CharField(max_length=200,verbose_name=_("نام ماده"))
    stuff_price_auto = models.BooleanField(default=True,verbose_name=_("بروزرسانی قیمت"))
    stuff_image = models.CharField(max_length=500,default="images/food/stuffs/none.jpg", verbose_name=_("آدرس تصویر گروه"))
    stuff_price = models.IntegerField(verbose_name=_("قیمت ماده به تومان"))
    stuff_group = models.ForeignKey(StuffGroup,on_delete=models.CASCADE,verbose_name=_("دسته‌بندی"))
    stuff_register_date = models.DateField(verbose_name=_("تاریخ ماده"),auto_now_add=True)
    stuff_update_date = models.DateTimeField(verbose_name=_("تاریخ آخرین ماده "),auto_now_add=True)
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"stuff_name","verbose_name":'نام ماده',"value":self.stuff_name},{"field_name":"stuff_price_auto","verbose_name":'بروزرسانی قیمت',"value":self.stuff_price_auto},{"field_name":"stuff_image","verbose_name":'تصویر ماده',"value":self.stuff_image},{"field_name":"stuff_price","verbose_name":'قیمت ماده',"value":self.stuff_price},{"field_name":"stuff_group","verbose_name":'دسته ماده',"value":self.stuff_group},{"field_name":"stuff_register_date","verbose_name":'تاریخ درج ماده',"value":self.stuff_register_date},{"field_name":"stuff_update_date","verbose_name":'تاریخ آپدیت ماده',"value":self.stuff_update_date}]
    def show_short_image_stuff(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.stuff_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_stuff.short_description = _("تصویر ماده")
    def __str__(self):
        return f"{self.stuff_name}"
    class Meta:
        verbose_name = _("ماده")
        verbose_name_plural = _("مواد")
        db_table ="table_stuff"
class Meal(models.Model):
    class_name = "Meal"
    meal_name = models.CharField(max_length=50,verbose_name=_("نام وعده غذایی"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"meal_name","verbose_name":'نام وعده غذایی',"value":self.meal_name}]
    def __str__(self):
        return f"{self.meal_name}"
    class Meta: 
        verbose_name = _("وعده غذایی")
        verbose_name_plural = _("وعده های غذایی")
        db_table ="table_food_meal"
        
def validate_recipes_video(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4','.mov','.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید docx ، mp4 یا webm باشد.'))
def validate_recipes_PDF_file(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید pdf باشد.'))
class Recipes(models.Model):
    class_name = "Recipes"
    recipe_image = models.ImageField(upload_to="images/food/recipes/",verbose_name=_("تصویر غذا"))
    recipe_slug = models.SlugField(max_length=120)
    recipe_stuffs = models.ManyToManyField(Stuff,verbose_name=_("مواد استفاده شده"))
    recipe = RichTextUploadingField(verbose_name=_("دستور پخت"),config_name='special')
    recipe_name = models.CharField(max_length=60,verbose_name=_("نام دستور"))
    recipe_summary_text = models.TextField(verbose_name=_("متن خلاصه دستور غذا"),help_text=_("در این قسمت باید یک خلاصه در مورد این دستور بنویسید. این متن در قسمت اشتراک گذاری به همراه لینک صفحه ارسال می شود."))
    recipe_key_words = models.ManyToManyField(KeyWord, verbose_name=_("کلمات کلیدی دستور غذا"),help_text=_("کلمات کلیدی مرتبط به این دستور غذا را انتخاب کنید. توجه کنید. باید کلمات کلیدی را به درستی انتخاب کنید تا سئو سایت به مشکل بر نخورد."),related_name = "recipe_key_words")
    recipe_file = models.FileField(upload_to='files/recipe/pdf',verbose_name=_("فایل پی دی اف دستور غذا"),help_text=_("در صورتی که این دستور غذا فایل پی دی اف داشت می توانید آن را بارگذاری کنید تا کاربران بتوانند آن را دانلود کنند."),null=True,blank=True,validators=[validate_recipes_PDF_file])
    recipe_short_url = models.URLField(max_length=200,verbose_name=_("لینک کوتاه"),null=True,blank=True,help_text=_("این قسمت را می توانید خالی بگذارید زیرا که سیستم خودکار این لینک را تولید می کند."))
    recipe_views = models.PositiveIntegerField(verbose_name=_("بازدیدها"))
    recipe_video =  models.FileField(upload_to='videos/Recipes/videos', verbose_name=_("ویدئو آمورزشی دستور"), validators=[validate_recipes_video],null=True,blank=True)
    recipe_likes = models.PositiveBigIntegerField(default=0, verbose_name=_('تعداد پسندیده‌ها شده'))
    recipe_dislikes = models.PositiveBigIntegerField(default=0, verbose_name=_('تعداد پسندیده‌ها نشده'))
    recipe_register_date = models.DateField(verbose_name=_("تاریخ ثبت دستور"),auto_now_add=True)
    recipe_publish_date = models.DateField(verbose_name=_("تاریخ انتشار دستور"),default=timezone.now)
    recipe_update_date = models.DateTimeField(verbose_name=_("تاریخ آخرین ویرایش دستور"),auto_now_add=True)
    recipe_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"recipe_image","verbose_name":'تصویر دستور غذا',"value":self.recipe_image},{"field_name":"recipe_slug","verbose_name":'اسلاگ دستور غذا',"value":self.recipe_slug},{"field_name":"recipe_stuffs","verbose_name":'تصویر دستور غذا',"value":(stuff for stuff in self.recipe_stuffs.all())},{"field_name":"recipe_name","verbose_name":'نام دستور غذا',"value":self.recipe_name},{"field_name":"recipe_views","verbose_name":'تعداد بازدید غذا',"value":self.recipe_views},{"field_name":"recipe_register_date","verbose_name":'تاریخ درج دستور غذا',"value":self.recipe_register_date},{"field_name":"recipe_publish_date","verbose_name":'تاریخ انتشار دستور غذا',"value":self.recipe_publish_date},{"field_name":"recipe_update_date","verbose_name":'تاریخ آپدیت دستورغذا',"value":self.recipe_update_date},{"field_name":"recipe_is_active","verbose_name":'فعال/غیرفعال',"value":self.recipe_is_active},]
    def __str__(self):
        return f"{self.recipe_name}"
    class Meta:
        verbose_name = _("دستور پخت")
        verbose_name_plural = _("دستورات پخت")
        db_table ="table_food_recipes"



class FoodStuffType(models.Model):
    class_name = "FoodStuffType"
    type_name = models.CharField(max_length=120,verbose_name=_("نام دسته"))
    stuffs = models.ManyToManyField(Stuff,verbose_name=_("ماده"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"type_name","verbose_name":'نام دسته',"value":self.type_name},{"field_name":"stuffs","verbose_name":'مواد',"value":(stuff for stuff in self.stuffs.all())}]
    def __str__(self):
        return f"{self.type_name}"
    class Meta:
        verbose_name = _("نوع ماده")
        verbose_name_plural = _("نوع مواد")
        db_table ="table_food_stuff_type"

class Food(models.Model):
    class_name = "Food"
    food_name = models.CharField(max_length=60,verbose_name=_("نام غذا"))
    food_slug = models.SlugField(max_length=120)
    food_image = models.ImageField(upload_to="images/food/food",verbose_name=_("تصویر غذا"))
    food_price  = models.IntegerField(verbose_name=_("قیمت غذا"),default=0)
    food_time = models.CharField(max_length=3,verbose_name=_("زمان پخت غذا"))
    food_wight = models.CharField(max_length=10,verbose_name=_("وزن غذا"))
    food_calories = models.CharField(max_length=10,verbose_name=_("کالری غذا"))
    food_description = models.TextField(verbose_name=_("توضیحات غذا"))
    food_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name="register date")
    food_sales_number = models.PositiveIntegerField(verbose_name=_("تعداد غذای فروخته شده"),default=0)
    food_views = models.PositiveIntegerField(verbose_name=_("تعداد بازدیدها"),default=0)
    food_recipes = models.ForeignKey(Recipes,on_delete=models.CASCADE,verbose_name=_("دستور پخت"))
    food_group = models.ForeignKey(FoodGroup,on_delete=models.CASCADE,verbose_name=_("دسته‌بندی"))
    food_stuff_types = models.ManyToManyField(FoodStuffType,verbose_name=_("گروه مواد استفاده شده"),blank=True)
    food_meal = models.ManyToManyField(Meal,verbose_name=_("وعده‌ی غذایی"))
    profit = models.PositiveIntegerField(verbose_name=_("سود حاصل از فروش این غذا"))
    is_auto_compile_price = models.BooleanField(default=True,verbose_name=_("به دست آوردن قیمت به صورت خودکار"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"food_name","verbose_name":'نام غذا',"value":self.food_name},{"field_name":"food_slug","verbose_name":'سلاگ غذا',"value":self.food_slug},{"field_name":"food_image","verbose_name":'تصویر غذا',"value":self.food_image},{"field_name":"food_price","verbose_name":'قیمت غذا',"value":self.food_price},{"field_name":"food_time","verbose_name":'زمان پخت غذا',"value":self.food_time},{"field_name":"food_wight","verbose_name":'وزن غذا',"value":self.food_wight},{"field_name":"food_calories","verbose_name":'کالری غذا',"value":self.food_calories},{"field_name":"food_description","verbose_name":'توضیحات غذا',"value":self.food_description},{"field_name":"register_date","verbose_name":'تاریخ درج غذا',"value":self.register_date},{"field_name":"food_sales_number","verbose_name":'تعداد غذای فروخته شده',"value":self.food_sales_number},{"field_name":"food_views","verbose_name":'تعداد بازدید از غذا',"value":self.food_views},{"field_name":"food_recipes","verbose_name":'دستور پخت غذا',"value":self.food_recipes},{"field_name":"food_group","verbose_name":'دسته غذا',"value":self.food_group},{"field_name":"food_stuff_types","verbose_name":'نوع مواد غذا',"value":self.food_stuff_types},{"field_name":"food_meal","verbose_name":'وعدهای مناسب غذا',"value":self.food_meal},{"field_name":"profit","verbose_name":'سود حاصل فروش غذا',"value":self.profit},{"field_name":"is_auto_compile_price","verbose_name":'قیمت غذا به صورت خودکار محاسبه شود؟',"value":self.is_auto_compile_price},{"field_name":"food_is_active","verbose_name":'فعال/غیرفعال',"value":self.food_is_active}]
    #  and dbd.discount_basket.start_date <= datetime.now() and datetime.now() >= dbd.discount_basket.end_date
    def get_price_by_discount(self):
        list_1 = []
        for dbd in self.food_discount_basket_detail_2.all():
            if dbd.discount_basket.is_active==True: 
                list_1.append(dbd.discount_basket.discount)
        discount = 0
        if len(list_1) > 0:
            discount=max(list_1)
        return int(self.food_price)-(int(self.food_price)*discount//100)
    def get_user_score(self):
        request = RequestMiddleware(get_response=None)
        request=request.thread_local.current_request 
        score = 0
        user_score  = self.scoring_food.filter(scoring_user=request.user)
        if user_score.count()>0:
            score.user_score[0].score
        return score
    # def get_average_score(self):
    #     avg_score = self.scoring_food.all().aggregate(Avg('score'))['score_avg']
    #     if avg_score==None:
    #         avg_score = 0
    #     return avg_score 
    def get_user_favorite(self):
        request = RequestMiddleware(get_response=None)
        request=request.thread_local.current_request
        flag = self.favorite_food.filter(favorite_user = request.user).exists()
        return flag
    def show_short_image_food(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.food_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_food.short_description = _("تصویر غذا")
    def __str__(self):
        return f"{self.food_name}"
    class Meta:
        verbose_name = _("غذا")
        verbose_name_plural = _("غذاها")
        db_table ="table_food"
class MyRecipes(models.Model):
    class_name = "MyRecipes"
    recipes_name = models.CharField(max_length=160,verbose_name=_("نام دستور"))
    recipes_price = models.PositiveIntegerField(verbose_name=_("قیمت"))
    recipes_register_date = models.DateField(verbose_name=_("تاریخ ذخیره سازی"),auto_now_add=True)
    recipes_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="کاربر")
    recipes_stuffs = models.ManyToManyField(Stuff,verbose_name=_("مواد استفاده شده"))
    recipes_food = models.ForeignKey(Food,on_delete=models.CASCADE,verbose_name=_("غذا"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"recipes_name","verbose_name":'نام دستور',"value":self.recipes_name},{"field_name":"recipes_price","verbose_name":'قیمت دستور',"value":self.recipes_price},{"field_name":"recipes_register_date","verbose_name":'تاریخ درج دستور',"value":self.recipes_register_date},{"field_name":"recipes_user","verbose_name":'کاربری که دستور را ساخته',"value":self.recipes_user},{"field_name":"recipes_food","verbose_name":'غذا',"value":self.recipes_food},{"field_name":"recipes_stuffs","verbose_name":'مواد',"value":(stuff for stuff in self.recipes_stuffs.all())}]
    def get_price_by_discount(self):
        list_1 = []
        for dbd in self.my_recipe_discount_basket_detail_2.all():
            if (dbd.discount_basket.is_active==True and dbd.discount_basket.start_date <= datetime.now() and datetime.now() >= dbd.discount_basket.end_date): 
                list_1.append(dbd.discount_basket.discount)
        discount = 0
        if len(list_1) > 0:
            discount=max(list_1)
        return self.recipes_price-(self.recipes_price*discount//100)
    def __str__(self):
        return f"{self.recipes_user} - {self.recipes_food} - {self.recipes_price}"
    class Meta:
        verbose_name = _("دستور پخت من")
        verbose_name_plural = _("دستورات پخت من")
        db_table ="table_food_my_recipes"
