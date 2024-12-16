# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='data_manager_app'
urlpatterns = [
    path('',index,name="index"),
    path('show-years-with-chart-title/',show_years_with_chart_title,name="show_years_with_chart_title"),
    path('show-months-with-year/',show_months_with_year,name="show_months_with_year"),
    path('show-days-with-month/',show_days_with_month,name="show_days_with_month"),
    # path('show-plot-image/',show_plot_image,name="show_plot_image"),
    
    path('create-or-update-languages/',create_or_update_languages,name="create_or_update_languages"),
    path('language-with-lang-code/',language_with_lang_code,name="language_with_lang_code"),
    path('language-with-lang-codes/',language_with_lang_codes,name="language_with_lang_codes"),
    
    path('create-or-update-currency/',create_or_update_currency,name="create_or_update_currency"),
    
    path('create-ro-update-stuffs-and-foods-price/',create_or_update_stuffs_and_foods_price,name="create_or_update_stuffs_and_foods_price"),
    
    path('create-or-update-country/',create_or_update_country,name="create_or_update_country"),
    path('create-or-update-cities/',create_or_update_cities,name="create_or_update_cities"),
    path('create-statistic-data/',create_statistic_data,name="create_statistic_data"),
    path('get-data-and-save-csv-format/',get_data_and_save_csv_format,name="get_data_and_save_csv_format"),
    path('show-plot/',show_plot,name="show_plot"),
    
    path('update-or-create-messages-language/', update_or_create_messages_language,name='update_or_create_messages_language'),
    
    path('create-or-update-css-fonts/', create_or_update_css_fonts,name='create_or_update_css_fonts'),
    
    path('send-sms-message-for-event/', send_sms_message_for_event,name='send_sms_message_for_event'),
    path('send-email-message-for-event/', send_email_message_for_event,name='send_email_message_for_event'),
    
    path('convert_image_format_to_webp/', convert_image_format_to_webp,name='convert_image_format_to_webp'),
]