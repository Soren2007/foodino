# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from Middleware.middleware import RequestMiddleware
from django.utils.translation import gettext_lazy as _
# from ckeditor.fields import RichTextField
# Create your models here.
class KeyWord(models.Model):
    class_name = "KeyWord"
    word = models.CharField(max_length=120,verbose_name=_("کلمه"),help_text=_("نکته: در انتخاب کلمه کلیدی بسیار دقت کنید تا از نظر سئو سایت به مشکل بر نخورد."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"word","verbose_name":'کلمه',"value":self.word}]
    def __str__(self):
        return f"{self.word}"
    class Meta:
        verbose_name = _("کلید‌واژه")
        verbose_name_plural = _("کلیدواژه‌ها")
        db_table ="table_key_words"
def validate_author_cv(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.docx']
    if not ext.lower()   in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید docx یا pdf باشد.'))
class Author(models.Model):
    class_name = "Author"
    author_avatar = models.ImageField(upload_to="images/blog/author/",verbose_name=_("آواتار"),help_text=_("لطفا غکس خود را بارگذاری کنید. نکته: بهتر است فرمت فایل بارگذاری شده webp باشد تا در سرعت سایت مشکلی پیش نیاید."))
    author_name = models.CharField(max_length=60, verbose_name=_("نام نویسنده"),help_text=_("نکته: لطفا نام خود را به زبان فارسی بنویسید."))
    author_family = models.CharField(max_length=60, verbose_name=_("نام خانوادگی نویسنده"),help_text=_("نکته: لطفا نام خانوادگی خود را به زبان فارسی بنویسید."))
    author_fullname = models.CharField(max_length=120,verbose_name=_("نام و نام خانوادگی نویسنده"),help_text=_("لطفا در وارد کردن نام و نام خانوادگی خود دقت فرمایید."))
    author_slug = models.SlugField(max_length=65, verbose_name=_("اسلاگ"),help_text=_("لطفا در وارد کردن اسلاگ بسیار دقت کنید. نکته: اسلاگ را باید به زبان انگلیسی وارد کنید و برای جدا سازی کلمات از - یا _ استفاده کنید."))
    author_email = models.EmailField(max_length=250, verbose_name=_("ایمیل"), null=True,help_text=_("لطفا ایمیل را با دقت وارد نمایید."))
    author_phone = models.CharField(max_length=14, default="+98", verbose_name=_("شماره موبایل"), null=True, help_text=_("شماره تماس را به درستی وارد کنید. نکته: نیازی به وارد کردن پیش شماره کشور نیست."))
    author_cv = models.FileField(upload_to='files/author/cv', verbose_name=_("رزومه"), validators=[validate_author_cv],help_text=_("لطفا رزومه خود را بارگذاری کنید. نکته: فرمت فایل باید docx و یا pdf  باشد."))
    author_info = models.TextField(verbose_name="توضیحات",help_text=_("لطفا توضیجی مختصر در مورد خود بنویسید."))
    author_is_active = models.BooleanField(default=False, verbose_name=_("وضعت فعال / غیرفعال"),help_text=_("شما با قعال و یا غیرفعال کردن این قسمت می توانید فعالیت نویسنده را کنترل کنید."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"author_avatar","verbose_name":'آواتار',"value":self.author_avatar},{"field_name":"author_name","verbose_name":'نام',"value":self.author_name},{"field_name":"author_family","verbose_name":'نام خانوادگی',"value":self.author_family},{"field_name":"author_fullname","verbose_name":'نام و نام‌خانوادگی',"value":self.author_fullname},{"field_name":"author_slug","verbose_name":'آواتار',"value":self.author_slug},{"field_name":"author_email","verbose_name":'آواتار',"value":self.author_email},{"field_name":"author_phone","verbose_name":'آواتار',"value":self.author_phone},{"field_name":"author_cv","verbose_name":'رزومه',"value":self.author_cv},{"field_name":"author_info","verbose_name":'درباره نویسنده',"value":self.author_info},{"field_name":"author_is_active","verbose_name":'فعال/غیرفعال',"value":self.author_is_active}]
    def show_short_image_author_avatar(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.author_avatar}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_author_avatar.short_description ="تصویر نویسنده"
    def __str__(self):
        return f"{self.author_name} {self.author_family}"
    class Meta:
        verbose_name =_("نویسنده")
        verbose_name_plural =_("نویسندگان")
        db_table ="table_authors"


def validate_article_PDF_file(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید pdf باشد.'))
class Article(models.Model):
    class_name = "Article"
    article_title = models.CharField(max_length=60, verbose_name=_("عنوان مقاله"),help_text=_("یکی از مهمترین بخش در سئو انتخاب درست عنوان یک مقاله است، پس به آن توجه کنید. نکته: عنوان مقاله باید دارای مفهوم باشد و با متن مقاله در ارتباط باشد."))
    article_slug = models.SlugField(max_length=200,help_text=_("لطفا در وارد کردن اسلاگ بسیار دقت کنید. نکته: اسلاگ را باید به زبان انگلیسی وارد کنید و برای جدا سازی کلمات از - یا _ استفاده کنید."))
    article_short_url = models.URLField(max_length=200,verbose_name=_("لینک کوتاه"),null=True,blank=True,help_text=_("این قسمت را می توانید خالی بگذارید زیرا که سیستم خودکار این لینک را تولید می کند."))
    article_main_image = models.ImageField(upload_to="images/blog/article",verbose_name=_("تصویر اصلی مقاله"),help_text=_("تصویر اصلی مقاله را بارگذاری کنید. این تصویر در نمایش مقالات و بالای مقاله به نمایش در می‌آید."))
    article_summary_text = models.TextField(verbose_name=_("متن خلاصه مقاله"),help_text=_("در این قسمت باید یک خلاصه در مورد این مقاله بنویسید. این متن در قسمت اشتراک گذاری به همراه لینک صفحه ارسال می شود."),null=True,blank=True) 
    article_main_text = RichTextUploadingField(verbose_name=_("متن اصلی مقاله"),config_name='special',help_text=_("در این قسمت محیطی در اختیار شما قرار گرفته است که می‌توانید متن مقاله را تایپ و ادیت کنید همچنین می‌توانید از جداول و ... به مقاله اضافه کنید."))
    article_key_words = models.ManyToManyField(KeyWord, verbose_name=_("کلمات کلیدی مقاله"),related_name="article_key_words",help_text=_("کلمات کلیدی مرتبط به این مقاله را انتخاب کنید. توجه کنید. باید کلمات کلیدی را به درستی انتخاب کنید تا سئو سایت به مشکل بر نخورد."),blank=True)
    article_register_date = models.DateField(verbose_name=_("تاریخ ثبت مقاله"),auto_now_add=True)
    article_publish_date = models.DateField(verbose_name=_("تاریخ انتشار مقاله"),default=timezone.now)
    article_update_date = models.DateTimeField(verbose_name=_("تاریخ آخرین ویرایش مقاله"),auto_now_add=True)
    article_read_time = models.IntegerField(verbose_name=_("مدت زمان مطالعه مقاله"),help_text=_("لطفا مقدار زمان برای مطالعه این مقاله را وارد کنید."))
    article_is_active = models.BooleanField(default=False, verbose_name=_("وضعت فعال / غیرفعال"),help_text=_("شما می‌توانید با فعال کردن این قسمت مجوز انتشار مقاله را صادر کنید."))
    article_file = models.FileField(upload_to='files/article/pdf',verbose_name=_("فایل پی دی اف مقاله"),help_text=_("در صورتی که این مقاله فایل پی دی اف داشت می توانید آن را بارگذاری کنید تا کاربران بتوانند آن را دانلود کنند."),null=True,blank=True,validators=[validate_article_PDF_file])
    article_visits = models.PositiveSmallIntegerField(default=0, verbose_name=_("تعداد بازدید"),editable=False,help_text=_("تعداد بازدید به صورت خودکار پر می شود."))
    article_group = models.CharField(max_length=200,verbose_name=_("گروه مقاله"),help_text=_("در این قسمت باید گروه مقاله را مشخص کنید. مثال: آموزشی"))
    article_author = models.ManyToManyField(Author,verbose_name=_("نویسنده مقاله"))
    article_likes = models.PositiveBigIntegerField(default=0, verbose_name=_('تعداد پسندیده‌ها شده'))
    article_dislikes = models.PositiveBigIntegerField(default=0, verbose_name=_('تعداد پسندیده‌ها نشده'))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"article_title","verbose_name":'عنوان',"value":self.article_title},{"field_name":"article_slug","verbose_name":'سلاگ',"value":self.article_slug},{"field_name":"article_short_url","verbose_name":'لینک کوتاه',"value":self.article_short_url},{"field_name":"article_main_image","verbose_name":'تصویر اصلی مقاله',"value":self.article_main_image},{"field_name":"article_summary_text","verbose_name":'خلاصه متن مقاله',"value":self.article_summary_text},{"field_name":"article_main_text","verbose_name":'متن اصلی مقاله',"value":self.article_main_text},{"field_name":"article_key_words","verbose_name":'کلمات کیلیدی مقاله',"value":"wd"},{"field_name":"article_register_date","verbose_name":'تاریخ ثبت مقاله',"value":self.article_register_date},{"field_name":"article_publish_date","verbose_name":'تاریخ انتشار مقاله',"value":self.article_publish_date},{"field_name":"article_update_date","verbose_name":'تاریخ آپدیت مقاله',"value":self.article_update_date},{"field_name":"article_read_time","verbose_name":'زمان مطالعه مقاله',"value":self.article_read_time},{"field_name":"article_is_active","verbose_name":'فعال/غیرفعال',"value":self.article_is_active},{"field_name":"article_file_name","verbose_name":'نام فایل مقاله',"value":self.article_file_name},{"field_name":"article_visits","verbose_name":'تعداد بازدید',"value":self.article_visits},{"field_name":"article_group","verbose_name":'دسته مقاله',"value":self.article_group},{"field_name":"article_author","verbose_name":'نویسنده مقاله',"value":""}]
    def show_short_image_article(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.article_main_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_article.short_description = _("تصویر مقاله")
    def get_user_favorite_blog(self):
        request = RequestMiddleware(get_response=None)
        request=request.thread_local.current_request
        flag = self.favorite_blog.filter(favorite_user = request.user).exists()
        return flag
    # (key_word for key_word in self.article_key_words.all())
    # (article_author for article_author in self.article_author.all())
    def __str__(self):
        return f"{self.article_title}"
    class Meta:
        verbose_name =_("مقاله")
        verbose_name_plural =_("مقالات")
        db_table ="table_articles" 