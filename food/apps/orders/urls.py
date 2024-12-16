# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name = "orders_app"
urlpatterns = [
    path('status-of-carts/', status_of_carts,name="status_of_carts"),
    path('carts/', CartsView.as_view(),name="carts"),
    path('show-carts/', show_carts,name="show_carts"),
    
    path('show-how-to-use/', show_how_to_use,name="show_how_to_use"),
    
    path('add-to-food-cart/', add_to_food_cart,name="add_to_food_cart"),
    path('add-to-my-recipe-cart/', add_to_my_recipe_cart,name="add_to_my_recipe_cart"),
    
    path('update-from-food-cart/', update_from_food_cart,name="update_from_food_cart"),
    path('update-from-my-recipe-cart/', update_from_my_recipe_cart,name="update_from_my_recipe_cart"),
    
    path('delete-form-food-cart/', delete_form_food_cart,name="delete_form_food_cart"),
    path('delete-form-my-recipe-cart/', delete_form_my_recipe_cart,name="delete_form_my_recipe_cart"),
    
    path('create-food-order/', CreateFoodOrderView.as_view(),name="create_food_order"),
    path('check-out-order/<int:order_id>/', CheckOutOrderView.as_view(),name="check_out_order"),
    path('apply-coupon/', apply_coupon,name="apply_coupon"),
    path('show-my-orders/', show_my_orders,name="show_my_orders"),
    path('show-cities-with-country/', show_cities_with_country,name="show_cities_with_country"),
    path('find-branch/', find_branch,name="find_branch"),
    
    path('orders-panel/', orders_panel,name="orders_panel"),
    path('order-details-panel/<int:order_id>/', order_details_panel,name="order_details_panel"),
    path('change-status-order/', change_status_order,name="change_status_order"),
    
    
    path('create-food-order/', CreateSubscriptionOrderView.as_view(),name="create_food_order"),
    
] 