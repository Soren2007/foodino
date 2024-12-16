from django.utils.translation import gettext_lazy as _

def create_random_code(count):
    from random import randint
    count-=1
    return randint(10**count,10**(count+1)-1)

def status_checker(status,request,redirect_name="main_app:index"):
        from django.contrib.messages import error,success
        from django.shortcuts import redirect
        if status == 200:
            return "ok"
        elif  status == 100 :
            error(request,_("درخواست‌کننده باید به درخواست خود ادامه دهد. سرور زمانی این کد را نمایش می‌دهد که بخش اول درخواست را دریافت کرده و منتظر بقیهٔ درخواست‌ها می‌باشد."),"error")
            return redirect(redirect_name)
        elif  status == 101 :
            error(request,_("درخواست‌کننده به سرور درخواست تعویض پروتکل‌ها را داده و سرور در حال تأیید کردن انجام تعویض است."),"error")
            return redirect(redirect_name)
        elif  status == 102 :
            error(request,_("سرور با ارسال کد ۱۰۲ به مرورگر، عملیات درخواستی را پردازش می‌کند."),"error")
            return redirect(redirect_name)
        elif  status == 201 :
            error(request,_("درخواست موفقیت آمیز بوده و سرور یک منبع جدید ایجاد کرده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 202 :
            error(request,_("سرور درخواست را پذیرفته، اما هنوز آن را محاسبه نکرده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 203 :
            error(request,_("	سرور با موفقیت درخواست را محاسبه کرده، اما اطلاعاتی را نمایش می‌دهد که ممکن است مربوط به منبع دیگری باشند."),"error")
            return redirect(redirect_name)
        elif  status == 204 :
            error(request,_("سرور با موفقیت درخواست را محاسبه کرده، اما هیچ محتوی ای را نمایش نمی‌دهد."),"error")
            return redirect(redirect_name)
        elif  status == 205 :
            error(request,_("سرور با موفقیت درخواست را محاسبه کرده، اما هیچ محتوی ای را نمایش نمی‌دهد. برخلاف کد ۲۰۴، این کد نیازمند این است که درخواست‌کننده نمای پرونده را تنظیم مجدد کند(برای مثال خالی کردن یک فرم)"),"error")
            return redirect(redirect_name)
        elif  status == 206 :
            error(request,_("سرور با موفقیت درخواست دریافت جزئی را پردازش کرده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 300 :
            error(request,_("سرور فعالیت‌های آماده‌ای بر اساس درخواست داده شده دارد. سرور ممکن است فعالیتی را بر اساس درخواست‌کننده انتخاب کند یا ممکن است لیستی از فعالیت‌هایی که درخواست‌کننده قادر به انتخاب آن هاست نمایش دهد."),"error")
            return redirect(redirect_name)
        elif  status == 301 :
            error(request,_("صفحه درخواست شده به‌طور دائم به مکان دیگری منتقل شده‌است. هنگامی که سرور این پاسخ را نمایش می‌دهد به‌طور خودکار درخواست‌کننده را به محل جدید انتقال می‌دهد."),"error")
            return redirect(redirect_name)
        elif  status == 302 :
            error(request,_("سرور در حال حاضر پاسخگو به در خواست صفحه‌ای در مکان دیگر می‌باشد، اما درخواست‌کننده باید برای درخواست‌های آینده به استفاده از مکان اصلی ادامه دهد."),"error")
        elif  status == 303 :
            error(request,_("سرور هنگامی این کد را نمایش می‌دهد که در خواست‌کننده باید درخواست جداگانهٔ دریافت را به محل دیگری برای دریافت پاسخ دهد."),"error")
            return redirect(redirect_name)
        elif  status == 304 :
            error(request,_("از هنگام آخرین درخواست، صفحهٔ درخواست شده اصلاح نشده‌است. هنگامی که سرور این پاسخ را نمایش می‌دهد، محتوی صفحه نمایش داده نخواهد شد."),"error")
            return redirect(redirect_name)
        elif  status == 305 :
            error(request,_("درخواست‌کننده زمانی می‌تواند به صفحه درخواست شده دسترسی داشته باشد که از پراکسی استفاده کند."),"error")
            return redirect(redirect_name)
        elif  status == 306 :
            error(request,_("این وضعیت همانند حالت کد ۳۰۵ است، با این تفاوت که درخواست مبتنی بر تعویض پراکسی"),"error")
            return redirect(redirect_name)
        elif  status == 307 :
            error(request,_("این کد مشابه کد ۳۰۲ عمل می‌کند."),"error")
            return redirect(redirect_name)
            
        elif  status == 400 :
            error(request,_("سرور قادر به تشخیص نحو (Syntax) درخواست نمی‌باشد."),"error")
            return redirect(redirect_name)
        elif  status == 401 :
            error(request,_("درخواست نیازمند تصدیق می‌باشد. سرور ممکن است این پاسخ را برای لاگین یک صفحه نمایش دهد."),"error")
            return redirect(redirect_name)
        elif  status == 402 :
            error(request,_("درخواست معتبر است، اما سرور قادر به انجام عملیات نیست. کاربر ممکن است مجوزهای لازم برای یک منبع را نداشته باشد یا ممکن است نیاز به حساب کاربری خاصی باشد."),"error")
            return redirect(redirect_name)
        elif  status == 403 :
            error(request,_("درخواست معتبر است، اما سرور قادر به انجام عملیات نیست. کاربر ممکن است مجوزهای لازم برای یک منبع را نداشته باشد یا ممکن است نیاز به حساب کاربری خاصی باشد."),"error")
            return redirect(redirect_name)
        elif  status == 404 :
            error(request,_("سرور قادر به پیدا کردن صفحه درخواست شده نمی‌باشد. برای مثال اگر برای صفحه‌ای که در سرور وجود ندارد درخواست شود، سرور اغلب این کد را نمایش می‌دهد."),"error")
            return redirect(redirect_name)
        elif  status == 405 :
            error(request,_("متود مشخص شده در درخواست مجاز نیست."),"error")
            return redirect(redirect_name)
        elif  status == 406 :
            error(request,_("صفحه درخواست شده قادر به پاسخ گویی به همراه مشخصه‌های محتوی درخواست شده نیست."),"error")
            return redirect(redirect_name)
        elif  status == 407 :
            error(request,_("این کد وضعیت مشابه کد ۴۰۱ می‌باشد؛ اما مشخص می‌کند که درخواست‌کننده برای استفاده از پراکسی نیاز به تصدیق دارد. زمانی که سرور این پاسخ را نمایش می‌دهد، همچنین به معنی پراکسی ای می‌باشد که درخواست‌کننده باید از آن استفاده کند."),"error")
            return redirect(redirect_name)
        elif  status == 408 :
            error(request,_("انتظار سرور برای درخواست به پایان رسیده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 409 :
            error(request,_("سرور برای انجام درخواست با ناسازگاری مواجه شده‌است. سرور باید شامل اطلاعاتی راجع به ناسازگاری در درخواست باشد."),"error")
            return redirect(redirect_name)
        elif  status == 410 :
            error(request,_("سرور این پاسخ را هنگامی نمایش می‌دهد که منبع درخواست شده به‌طور دائم حذف شده باشد. این کد مشابه کد ۴۰۴ می‌باشد، اما گاهی اوقات به جای کد ۴۰۴، برای منابعی که دیگر وجود ندارند به کار برده می‌شود."),"error")
            return redirect(redirect_name)
        elif  status == 411 :
            error(request,_("سرور درخواست را بدون طول محتوی فیلد هدر نمی‌پذیرد."),"error")
            return redirect(redirect_name)
        elif  status == 412 :
            error(request,_("سرور با یکی از پیش شرط‌هایی که درخواست به‌کننده در درخواست قرار داده مواجه نشده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 413 :
            error(request,_("سرور قادر به پردازش به دلیل بزرگی درخواست برای رسیدگی نیست."),"error")
            return redirect(redirect_name)
        elif  status == 414 :
            error(request,_("یوآرال در خواست شده برای پردازش توسط سرور بسیار طولانی است."),"error")
            return redirect(redirect_name)
        elif  status == 415 :
            error(request,_("درخواست به شکلی است که توسط صفحه درخواست‌کننده پشتیبانی نمی‌شود."),"error")
            return redirect(redirect_name)
        elif  status == 416 :
            error(request,_("اگر درخواست برای محدوده‌ای باشد که برای صفحه در دسترس نیست، سرور این کد وضعیت نمایش می‌دهد."),"error")
            return redirect(redirect_name)
        elif  status == 417 :
            error(request,_("سرور قادر به مواجه شدن با انتظار فیلد هدر درخواست نمی‌باشد."),"error")
            return redirect(redirect_name) 
        elif  status == 500 :
            error(request,_("سرور با خطا مواجه شده و قادر به انجام درخواست نمی‌باشد."),"error")
            return redirect(redirect_name)
        elif  status == 501 :
            error(request,_("سرور قابلیت انجام درخواست را ندارد. برای مثال سرور ممکن است این کد را زمانی نمایش دهد که قادر به شناسایی متود درخواست نباشد."),"error")
            return redirect(redirect_name)
        elif  status == 502 :
            error(request,_("سرور مانند درگاه یا پراکسی عمل کرده و پاسخ اشتباهی از سرور بالا دست دریافت کرده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 503 :
            error(request,_("سرور در حال حاضر در دسترس نمی‌باشد. (به دلیل این که برای تعمیر یا گرانبار شده یا از کار افتاده). به‌طور کل این وضعیت موقتی می‌باشد."),"error")
            return redirect(redirect_name)
        elif  status == 504 :
            error(request,_("سرور مانند درگاه یا پراکسی عمل کرده و درخواست به موقع ای از سرور بالا دست دریافت نکرده‌است."),"error")
            return redirect(redirect_name)
        elif  status == 505 :
            error(request,_("سرور نگارش پروتکل HTTP موجود در درخواست را پشتیبانی نمی‌کند."),"error")
            return redirect(redirect_name)
        else:
            error(request,_("خطا در انجام عملیات!"),"error")
            return redirect(redirect_name)
def send_sms(request,mobile_number, message,redirect_name="main_app:index"):
    from ghasedakpack import Ghasedak
    sms = Ghasedak("1832612702d4bbbe12107c6205746031aa07a78d0ba13af9e44ca36ea0d1cee2")
    status = sms.send({'message':str(message), 'receptor' : f'{mobile_number}', 'linenumber': '10008566' })
    status_checker(int(status),request,redirect_name)
    return status
def price_by_delivery_tax(price,discount=0):
    delivery = 25000
    if price > 500000:
        delivery=0
    tax = (price+delivery)*0.09
    sum = price+delivery+tax
    sum = sum-(sum*discount/100)
    return int(sum),delivery,int(tax)

from django.core.mail import send_mail
from apps.accounts.models import CustomUser
class Send_Email:
    def __init__(self,request,subject,message,from_email):
        self.request = request
        self.subject=subject
        self.message=message
        self.from_email=from_email
        
    def send_email_ads(self):
        emails = []
        for user in CustomUser.objects.all():
            if user.email != "":
                emails.append(user.email)
        send_mail(
        str(self.subject),
        str(self.message),
        str(self.from_email),
        emails,
        fail_silently=False)


import requests
class Scrap:
    def __init__(self,url,request):
        from bs4 import BeautifulSoup
        self.url = url
        self.request=request
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.content, "html.parser")
        self.objects = []
    def scrap_stuffs(self): 
        from re import findall 
        from string import ascii_lowercase,ascii_uppercase
        if status_checker(self.res.status_code,self.request) == "ok":
            prices = self.soup.select(".prd-price>span")
            stuffs = self.soup.select(".maintitle")
            images = self.soup.select(".prd-ax img") # pattern = "lazysrc=\"(.*) "
            for i in range(len(prices)):
                image_url = findall(r"lazysrc=\"(.*)\" d",str(images[i]))
                if len(image_url) == 0:
                    image_url = "https://img.icons8.com/?size=1x&id=zGSj13jiurKj&format=png"
                stuff_name = stuffs[i].text
                stuff_name = stuff_name.replace('گرمی','')
                stuff_name = stuff_name.replace('گرم','')
                stuff_name = stuff_name.replace('یک کیلویی','')
                stuff_name = stuff_name.replace('کیلوگرمی','')
                stuff_name = stuff_name.replace('وزن','')
                stuff_name = stuff_name.replace('فله ای','')
                stuff_name = stuff_name.replace('درصد','')
                stuff_name = stuff_name.replace('کیلو','')
                stuff_name = stuff_name.replace('مقدار','')
                stuff_name = stuff_name.replace('0','')
                stuff_name = stuff_name.replace('1','')
                stuff_name = stuff_name.replace('2','')
                stuff_name = stuff_name.replace('3','')
                stuff_name = stuff_name.replace('4','')
                stuff_name = stuff_name.replace('5','')
                stuff_name = stuff_name.replace('6','')
                stuff_name = stuff_name.replace('7','')
                stuff_name = stuff_name.replace('8','')
                stuff_name = stuff_name.replace('9','')
                stuff_name = stuff_name.replace('۰','')
                stuff_name = stuff_name.replace('۱','')
                stuff_name = stuff_name.replace('۲','')
                stuff_name = stuff_name.replace('۳','')
                stuff_name = stuff_name.replace('۴','')
                stuff_name = stuff_name.replace('۵','')
                stuff_name = stuff_name.replace('۶','')
                stuff_name = stuff_name.replace('۷','')
                stuff_name = stuff_name.replace('۸','')
                stuff_name = stuff_name.replace('۹','')
                stuff_name = stuff_name.replace('gr','')
                stuff_name = stuff_name.replace('kg','')
                stuff_name = stuff_name.replace('%','')
                stuff_name = stuff_name.replace('%','')
                stuff_name = stuff_name.replace('۲','')
                stuff_name = stuff_name.replace('10کیلوگرم','')
                stuff_name = stuff_name.replace('.','')
                stuff_name = stuff_name.replace('/','')
                stuff_name = stuff_name.replace('-','')
                stuff_name = stuff_name.replace(')','')
                stuff_name = stuff_name.replace('(','')
                stuff_name = stuff_name.replace('}','')
                stuff_name = stuff_name.replace('{','')
                stuff_name = stuff_name.replace('|','')
                stuff_name = stuff_name.replace('/','')
                stuff_name = stuff_name.replace('–','')
                stuff_name = stuff_name.replace('  ',' ')
                for ch in ascii_lowercase:
                    stuff_name = stuff_name.replace(ch,'')
                for ch in ascii_uppercase:
                    stuff_name = stuff_name.replace(ch,'')
                self.objects.append({"stuff_price":int((prices[i].text).replace(',','')),"stuff_name":stuff_name,"stuff_image_url":image_url})
            return self.objects
    
    
    def scrap_countries(self):
        if status_checker(self.res.status_code,self.request) == "ok":
            telephone_codes = self.soup.select(".wp-block-table tbody > tr > td:nth-child(1)")
            names = self.soup.select(".wp-block-table tbody > tr > td:nth-child(2)")
            for i in range(len(telephone_codes)):
                name = names[i].text
                name = name.replace('کشور','')
                name = name.replace('کد','')
                name = name.replace('  ','')
                self.objects.append({"name":name,"telephone_code":telephone_codes[i].text})
            return self.objects
        
        
    def scrap_states(self):   
        if status_checker(self.res.status_code,self.request) == "ok":
            telephone_codes = self.soup.select(".table-is-responsive>table>tbody>tr>td:nth-child(1)")
            names = self.soup.select(".table-is-responsive>table>tbody>tr>td:nth-child(2)")
            for i in range(len(telephone_codes)):
                self.objects.append({"name":names[i].text,"telephone_code":telephone_codes[i].text})
            return self.objects
        
    def scrap_cities(self,selector='.wikitable td:nth-child(2) a'):   
        if status_checker(self.res.status_code,self.request) == "ok":
            #  tbody td:nth-child({td_nth_child_number}) a
            cities_name = self.soup.select(selector)
            for i in range(len(cities_name)):
                # print(cities_name[i].text)
                self.objects.append({"city_name":cities_name[i].text})
            return self.objects
    def scrap_language(self):   
        if status_checker(self.res.status_code,self.request) == "ok":
            language_code = self.soup.select("tbody td:nth-child(1)")
            language_name = self.soup.select("tbody td:nth-child(2)")
            language_directionality = self.soup.select("tbody td:nth-child(3)")
            for i in range(len(language_code)):
                self.objects.append({"language_code":str(language_code[i].text).replace("\n",""),"language_name":str(language_name[i].text).replace("\n",""),"language_directionality":str(language_directionality[i].text).replace("\n","")})
            return self.objects
        
    def scrap_currencies(self):   
        if status_checker(self.res.status_code,self.request) == "ok":
            country_name = self.soup.select("tbody tr:nth-child(n+3) td:nth-child(1)")
            currency = self.soup.select("tbody tr:nth-child(n+3) td:nth-child(2)")
            ISO_code = self.soup.select("tbody tr:nth-child(n+3) td:nth-child(3)")
            symbol = self.soup.select("tbody tr:nth-child(n+3) td:nth-child(4)")
            for i in range(len(country_name)):
                self.objects.append({"country_name":str(country_name[i].text).replace("\n",""),"currency":str(currency[i].text).replace("\n",""),"ISO_code":str(ISO_code[i].text).replace("\n",""),"symbol":str(symbol[i].text).replace("\n","")})
            return self.objects
             
class QR:
    def __init__(self, qr_text:str, qr_color:str, qr_scale:int,qr_save_dir:str,qr_save_name:str,qr_save_format:str):
        self.qr_text = str(qr_text)
        self.qr_color = str(qr_color)
        self.qr_scale = int(qr_scale)
        self.qr_save_dir = str(qr_save_dir)
        self.qr_save_name = str(qr_save_name)
        self.qr_save_format = str(qr_save_format)
    def create_qr(self):
        from pyqrcode import create
        url = create(self.qr_text)
        url.png(f"{self.qr_save_dir}/{self.qr_save_name}.{self.qr_save_format}", scale=self.qr_scale,
        module_color = self.qr_color)
        return "ok"

from shutil import copyfileobj
def image_saver(img_url,dir,file_name,format):
    res = requests.get(img_url, stream = True)
    print(100*"--")
    if res.status_code == 200:
        with open(f"{dir}/{file_name}{format}",'wb') as f:
            copyfileobj(res.raw, f) 
            print('Image sucessfully Downloaded: ',file_name)
    print('Image Couldn\'t be retrieved')

from pandas import *
from matplotlib.pyplot import *
from colorama import Fore
from sys import exit
class Plot:
    def __init__(self,csv_file_dir,csv_file_name,x_label,y_label,plot_title):
        try:
            self.data =  read_csv(csv_file_dir+'/'+csv_file_name+".csv") 
        except Exception as error:
            print(Fore.RED+f"{error}")
        # subplot(1,3,1)
        xlabel(x_label)
        ylabel(y_label)
        title(plot_title)
        print(self.data['food views'])
        views=self.data.groupby(['food views'])
        plot(self.data['date'],self.data['food views'],color="pink",
        label='Room 1 Temperature at Mehr',marker='o',
        ms=4,mfc='r',mec='r',linewidth=0.8)
        savefig('food_view_plote')
        return ""
# Plot('C:/Users/asus/Desktop/Programming/nojavankharazmi/food/media/files/csv/2023-06-20','food','تعداد غذای فروخته شده','Day'," تعداد غذای فروخته شده")
class Data:
    """Data class"""
    def __init__(self,filePath):
        self.__filePath=filePath
        self.fA=self.readFile('A').fillna(0)
        self.fB=self.readFile('B')
        self.fC=self.readFile('C')
        self.mainDataFrame = merge(merge(self.fA,self.fB,how='outer'),self.fC,how='outer')
        print(self.mainDataFrame)
    def readFile(self,char):
        try:
            return read_csv(self.__filePath+'/product_'+char+'.csv') 
        except Exception as error:
            print(Fore.RED+f"{error}")
        
    def showBars(self):
        name=self.mainDataFrame.groupby(['Code'])['Name'].max()
        view=self.mainDataFrame.groupby(['Code'])['View'].max()
        like=self.mainDataFrame.groupby(['Code'])['Like'].max()
        order=self.mainDataFrame.groupby(['Code'])['Order'].max()
        subplot(1,3,1)
        xlabel('Name')
        ylabel("Values")
        title('Views')
        bar(name,view,color='pink')
        subplot(1,3,2)
        xlabel('Name')
        ylabel("Values")
        title('Likes')
        bar(name,like,color='orange')
        subplot(1,3,3)
        xlabel('Name')
        ylabel("Values")
        title('Orders')
        bar(name,order,color='red')
        show()
    def showPlots(self):
        subplot(1,3,1)
        xlabel('Day')
        ylabel("Values")
        title('ProductA')
        plot(self.fA['Day'],self.fA['Order'],color="pink")
        subplot(1,3,2)
        xlabel('Day')
        ylabel("Values")
        title('ProductB')
        plot(self.fB['Day'],self.fB['Order'],color="orange")
        subplot(1,3,3)
        xlabel('Day')
        ylabel("Values")
        title('ProductC')
        plot(self.fC['Day'],self.fC['Order'],color="red")
        show()
        

def text_sorting(text):
    text=text.replace("\n", "")
    text=text.replace("\r", "")
    text=text.replace('""', '"')
    text=text.replace('  ', ' ')
    return text

from re import findall
from os.path import exists
from os import chdir
from subprocess import getoutput
from django.conf import settings
from googletrans import Translator
from threading import Thread
from time import sleep
from apps.language.models import Language
from django.core.exceptions import ObjectDoesNotExist
class Translator_Language:
    def __init__(self,to_lang="en"):
        from datetime import datetime
        self.is_makemessages = False
        self.msgids = []
        self.translator=Translator()
        self.to_lang = to_lang
        self.django_po_file_data = f"""# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: {datetime.now()}\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n
"""
    def add_django_po_data(self,msgid,msgstr):
        if msgstr == None:
            try:
                text=self.translator.translate(msgid,dest=f'{self.to_lang}').text
                text=text.replace('"', "'")
                text=text.replace('\\', "")
                text=text.replace('﻿', "")
                if text != "" or msgid != "":
                    self.django_po_file_data+=f'msgid "{msgid}"\nmsgstr "{text}"\n'
            except Exception as error:
                print(error)
                if msgstr != "" or msgid != "":
                    self.django_po_file_data+=f'msgid "{msgid}"\nmsgstr "{str(msgstr)}"\n'
        else:
            if msgstr != "" or msgid != "":
                self.django_po_file_data+=f'msgid "{msgid}"\nmsgstr "{msgstr}"\n'
        self.write_po_file()
            
    def write_po_file(self,mod="w"):
        if self.is_makemessages != False:
            with open(f'{settings.LOCALE_PATHS[0]}\\{self.to_lang}\\LC_MESSAGES\\django.po',mod,encoding="UTF-8") as po_file:
                po_file.write(self.django_po_file_data)
            # self.compilemessages(self.to_lang)
        else:
            self.makemessages(language_code=self.to_lang)
        
    def compilemessages(self,language_code=None):
        chdir(settings.BASE_DIR)
        if language_code == None:
            getoutput('python manage.py compilemessages')
        else:
            getoutput(f'python manage.py compilemessages -l {language_code}')
            
    def makemessages(self,language_code=None):
        chdir(settings.BASE_DIR)
        print(f'python manage.py makemessages -l {language_code}')
        if language_code == None:
            getoutput('python manage.py makemessages --all')
        else:
            getoutput(f'python manage.py makemessages -l {language_code}')
            try:
                language = Language.objects.get(language_code = self.to_lang)
                languagelanguage_is_active = True
            except ObjectDoesNotExist:
                Language.objects.create(language_code = self.to_lang).save()
            except:
                pass
            
        self.is_makemessages = True
           
    def translate_values_of_models(self):
        from apps.accounts.models import Country,State,City
        from apps.ad.models import Ad
        from apps.blog.models import Author,Article,KeyWord
        from apps.branch.models import Branch
        from apps.comments.models import Comment
        from apps.discounts.models import DiscountBasket
        from apps.Email.models import Email
        from apps.event.models import Event,Top_Menu_Event,Footer_Event
        from apps.food.models import Food, Recipes,FoodStuffType,Meal,Stuff,StuffGroup,FoodGroup
        from apps.gift.models import Lottery,Gift,wheel_of_luck
        from apps.main.models import Slid,frequently_asked_question
        from apps.message.models import Message,UserChatRoom,ChatRoom
        from apps.mukbang.models import Mukbang
    
        # accounts app 
        thread_active_number = 0
        for country in Country.objects.all():
            msgid = country.name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            country.is_translated_content = True 
            country.save()
                # self.add_django_po_data(msgid,None)
                
        thread_active_number = 0
        for state in State.objects.all():
            msgid = state.name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                # self.add_django_po_data(msgid,None)
            state.is_translated_content = True 
            state.save()
             
        thread_active_number = 0
        for city in City.objects.all():
            msgid = city.name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            city.is_translated_content = True 
            city.save()
                
        for custom_user in CustomUser.objects.all():
            msgid = custom_user.name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            msgid = custom_user.family
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            msgid = custom_user.address
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            custom_user.is_translated_content = True 
            custom_user.save()
        # ad app 
        for ad in Ad.objects.all():
            msgid = ad.ad_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            ad.is_translated_content = True 
            ad.save()
                
        # blog app        
        for article in Article.objects.all():  
            msgid = article.article_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                
            msgid = article.article_summary_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                
            text=str(article.article_main_text)
            text=text.replace('\n',"")
            text=text.replace('\r',"")
            text=text.replace(' \n ',"")
            text=text.replace('"',"'")
            text=text.replace('  '," ")
            msgid = text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                
            article.article_main_text=text
            article.is_translated_content = True 
            article.save()
        for author in Author.objects.all():
            msgid = author.author_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            msgid = author.author_family
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            msgid = author.author_fullname
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            msgid = author.author_info
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            author.is_translated_content = True 
            author.save() 
        for key_word in KeyWord.objects.all():
            msgid = key_word.word
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
        key_word.is_translated_content = True 
        key_word.save()
        # branch app 
        for branch in Branch.objects.all():
            msgid = branch.branch_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = branch.branch_address
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            branch.is_translated_content = True 
            branch.save()
        # comment app 
        for comment in Comment.objects.all():
            msgid = comment.comment_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            comment.is_translated_content = True 
            comment.save()
            
        # DiscountBasket app 
        for discount_basket in DiscountBasket.objects.all():
            msgid = discount_basket.discount_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            discount_basket.is_translated_content = True 
            discount_basket.save()
            
        # Email app 
        for email in Email.objects.all():
            msgid = email.subject
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = email.message
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            email.is_translated_content = True 
            email.save()
            
        # Event app 
        for event in Event.objects.all():
            msgid = event.event_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = event.event_action_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = event.event_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            event.is_translated_content = True 
            event.save()
        for top_menu_event in Top_Menu_Event.objects.all():
            msgid = top_menu_event.event_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = top_menu_event.event_action_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            top_menu_event.is_translated_content = True 
            top_menu_event.save()
        for footer_event in Footer_Event.objects.all():
            msgid = footer_event.event_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = footer_event.event_action_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            footer_event.is_translated_content = True 
            footer_event.save()
            
        # food app  
        for food in Food.objects.all():
            msgid = food.food_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                
            msgid = food.food_description
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            food.is_translated_content = True 
            food.save()
        for recipe in Recipes.objects.all():
            msgid = recipe.recipe_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                 
            text=str(recipe.recipe)
            text=text.replace('\n',"")
            text=text.replace('\r',"")
            text=text.replace(' \n ',"")
            text=text.replace('"',"'")
            text=text.replace('  '," ")
            msgid = text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            recipe.recipe=text
            recipe.is_translated_content = True 
            recipe.save()
            
        for food_stuff_type in FoodStuffType.objects.all():
            msgid = food_stuff_type.type_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            food_stuff_type.is_translated_content = True 
            food_stuff_type.save()
                
        for meal in Meal.objects.all():
            msgid = meal.meal_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            meal.is_translated_content = True 
            meal.save()
                
        for stuff in Stuff.objects.all():
            msgid = stuff.stuff_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            stuff.is_translated_content = True 
            stuff.save()
                
        for stuff_group in StuffGroup.objects.all():
            msgid = stuff_group.group_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            stuff_group.is_translated_content = True 
            stuff_group.save()
                
        for food_group in FoodGroup.objects.all():
            msgid = food_group.group_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            food_group.is_translated_content = True 
            food_group.save()
        
        # Gift app  
        for lottery in Lottery.objects.all():
            msgid = lottery.title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
                
            
            text=str(lottery.description)
            text=text.replace('\n',"")
            text=text.replace('\r',"")
            text=text.replace(' \n ',"")
            text=text.replace('"',"'")
            text=text.replace('  '," ") 
            msgid = text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            lottery.description=text
            lottery.is_translated_content = True 
            lottery.save()
            
        for gift in Gift.objects.all():
            msgid = gift.title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = gift.description
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            gift.is_translated_content = True 
            gift.save()
        for wheel_of_luck in wheel_of_luck.objects.all():
            msgid = wheel_of_luck.title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = wheel_of_luck.description
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            wheel_of_luck.is_translated_content = True 
            wheel_of_luck.save()

        # main app  
        for slid in Slid.objects.all():
            msgid = slid.slid_title
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            slid.is_translated_content = True 
            slid.save()
            
        for f_a_q in frequently_asked_question.objects.all():
            text=str(f_a_q.question)
            text=text.replace('\n',"")
            text=text.replace('\r',"")
            text=text.replace(' \n ',"")
            text=text.replace('"',"'")
            text=text.replace('  '," ") 
            msgid = text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            
            text=str(f_a_q.response)
            text=text.replace('\n',"")
            text=text.replace('\r',"")
            text=text.replace(' \n ',"")
            text=text.replace('"',"'")
            text=text.replace('  '," ") 
            msgid = text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            f_a_q.question=text
            f_a_q.response=text
            f_a_q.is_translated_content = True 
            f_a_q.save()
                
        # message app
        for message in Message.objects.all():
            msgid = message.name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = message.family
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            msgid = message.subject
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            message.is_translated_content = True 
            message.save()   
        for user_chat_room in UserChatRoom.objects.all():
            msgid = user_chat_room.full_name
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            user_chat_room.is_translated_content = True 
            user_chat_room.save()   
                
        for chat_room in ChatRoom.objects.all():
            msgid = chat_room.message_text
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            chat_room.is_translated_content = True 
            chat_room.save()
                
        # mukbang app
        for mukbang in Mukbang.objects.all():
            msgid = mukbang.description
            if msgid not in self.msgids:
                self.msgids.append(msgid)
                Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                sleep(0.04)
            mukbang.is_translated_content = True 
            mukbang.save()

                  
    def translate_po_files(self):
        self.makemessages(language_code=self.to_lang)
        po_file_path = f'{settings.LOCALE_PATHS[0]}\\{self.to_lang}\\LC_MESSAGES\\django.po'
        if exists(po_file_path):
            try:
                with open(po_file_path,'r',encoding="UTF-8") as r_language_po_messages:
                    po_file_text = r_language_po_messages.read()
                    po_file_text=po_file_text.replace("\n", "")
                    po_file_text=po_file_text.replace("\r", "")
                    po_file_text=po_file_text.replace('msgstr ""', 'msgstr " "')
                    po_file_text=po_file_text.replace('""', '"')
                    po_file_text=po_file_text.replace('msgid "', '\nmsgid "')
                    po_file_text=po_file_text.replace('msgstr " "', '\nmsgstr " "')
                    po_file_text=po_file_text.replace('#:', '\n#:')
                    for msgid in findall(r'msgid \"(.*)\"',po_file_text):
                        msgid = msgid.replace('"msgstr','')
                        msgid=msgid.replace('"', "'")
                        if msgid not in self.msgids:
                            self.msgids.append(msgid)
                            # self.add_django_po_data(msgid,None)
                            Thread(target=self.add_django_po_data,args=[msgid,None]).start()
                            sleep(0.04)
            except Exception as error:
                print(error)
    def get_data_of_django_po_file(self,po_file_path) -> list:
        with open(po_file_path,'r',encoding="UTF-8") as r_language_po_messages:
            po_file_text = r_language_po_messages.read()
            po_file_text=po_file_text.replace("\n", "")
            po_file_text=po_file_text.replace("\r", "")
            po_file_text=po_file_text.replace('msgstr ""', 'msgstr " "')
            po_file_text=po_file_text.replace('""', '"')
            po_file_text=po_file_text.replace('msgid "', '\nmsgid "')
            po_file_text=po_file_text.replace('msgstr " "', '\nmsgstr " "')
            po_file_text=po_file_text.replace('#:', '\n#:')
            data_list = findall(r'msgid \"(.*)\"',po_file_text)
        return data_list
    def add_data_po_file(self,text):
        po_file_path = f'{settings.LOCALE_PATHS[0]}\\{self.to_lang}\\LC_MESSAGES\\django.po'
        if exists(po_file_path):
            with open(po_file_path,'a',encoding="UTF-8") as a_language_po_messages:
                if text not in self.get_data_of_django_po_file(po_file_path):
                    msgstr = ""
                    msgstr=self.translator.translate(text,dest=f'{self.to_lang}').text
                    msgstr=msgstr.replace('"', "'")
                    msgstr=msgstr.replace('\\', "")
                    msgstr=msgstr.replace('﻿', "")
                    po_data = f"""msgid "{text}"\nmsgstr "{msgstr}"\n"""
                    a_language_po_messages.write(po_data)
                    print(po_data)
                    self.compilemessages(self.to_lang)
                    return msgstr
        
    
    
from PIL import Image
from os.path import splitext
class ImageProcessing:
    def __init__(self,image_path) -> None:
        self.image_path = image_path
        self.image_path = self.image_path.replace("\\", "/")
        self.image_dir,self.image_ext = splitext(self.image_path)
        self.image = Image.open(self.image_path)
        self._image_heigth,self._image_width = self.image.size
        print(self.image_dir)
        print(self.image_ext)
    def compress_image(self,format):
        self.image.resize((self._image_heigth,self._image_width), Image.ANTIALIAS).save(f"{self.image_dir}.{format}")
    