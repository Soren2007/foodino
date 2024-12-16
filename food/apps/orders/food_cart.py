# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from apps.food.models import Food,MyRecipes,Recipes
class FoodCart:
    def __init__(self,request):
        self.request = request
        # self.request.session['food_data_cart'] = {}
        self.session = self.request.session
        try:
            food_data_temp=self.session['food_data_cart']
            if not food_data_temp:
                food_data_temp = self.session['food_data_cart'] = {}
        except:
            food_data_temp=self.session['food_data_cart'] = {}
        self.food_cart_objects = food_data_temp
        self.food_count=len(self.food_cart_objects.keys())
        
    def add_to_food_cart(self,food,qty,how_to_use):
        food_id = str(food.id)
        if food_id not in self.food_cart_objects:
            self.food_cart_objects[food_id]={"qty":0,"how_to_use":how_to_use,"price":int(food.food_price),"final_price":food.get_price_by_discount()}
        self.food_cart_objects[food_id]['qty']+=int(qty)
        self.food_count=len(self.food_cart_objects.keys())
        self.session.modified = True
    
    def update_from_food_cart(self,food,qty):
        food_id = str(food.id)
        self.food_cart_objects[food_id]['qty']=int(qty)
        self.session.modified = True
    
    def delete_from_food_cart(self,food):
        food_id = str(food.id)
        del self.food_cart_objects[food_id]
        self.session.modified = True
        
    def delete_all_food_carts(self):
        self.request.session['food_data_cart'] = {}
        
    def calc_total_price(self):
        sum=0
        for item in self.session.get('food_data_cart').values():
            sum+=(int(item['final_price'])*int(item['qty']))
        return sum
    def __iter__(self):
        food_list_id = self.food_cart_objects.keys()
        foods = Food.objects.filter(id__in=food_list_id)
        food_data_temp = self.food_cart_objects.copy()
        for food in foods:
            food_data_temp[str(food.id)]['food']={"id":food.id,"food_name":food.food_name,"food_slug":food.food_slug,"food_image":f"{food.food_image}","food_price":food.food_price,"food_time":food.food_time,"food_wight":food.food_wight,"food_calories":food.food_calories,"food_description":food.food_description,"food_is_active":food.food_is_active,"register_date":str(food.register_date),"food_sales_number":food.food_sales_number}
        for item in food_data_temp.values():
            item['total_price']=int(item['final_price'])*item['qty']
            yield item
    
class MyRecipeCart:
    def __init__(self,request):
        self.request = request
        # self.request.session['my_recipes_data_cart'] = {}
        self.session = self.request.session
        try:
            my_recipes_data_temp=self.session['my_recipes_data_cart']
            if not my_recipes_data_temp:
                my_recipes_data_temp = self.session['my_recipes_data_cart'] = {}
        except:
            my_recipes_data_temp=self.session['my_recipes_data_cart'] = {}
        self.my_recipes_cart_objects = my_recipes_data_temp
        self.my_recipes_count=len(self.my_recipes_cart_objects.keys())
        
    def add_to_my_recipe_cart(self,my_recipe,qty,how_to_use):
        my_recipe_id = str(my_recipe.id)
        if my_recipe_id not in self.my_recipes_cart_objects:
            self.my_recipes_cart_objects[my_recipe_id]={"qty":0,"how_to_use":how_to_use,"price":my_recipe.recipes_price,"final_price":my_recipe.recipes_price}
        self.my_recipes_cart_objects[my_recipe_id]['qty']+=int(qty)
        self.my_recipes_count=len(self.my_recipes_cart_objects.keys())
        self.session.modified = True
        
    def update_from_my_recipe_cart(self,my_recipe,qty):
        my_recipe_id = str(my_recipe.id)
        self.my_recipes_cart_objects[my_recipe_id]['qty']=int(qty)
        self.session.modified = True
        
    def delete_from_my_recipe_cart(self,my_recipe):
        my_recipe_id = str(my_recipe.id)
        del self.my_recipes_cart_objects[my_recipe_id]
        self.session.modified = True
    def delete_all_my_recipe_carts(self):
        self.request.session['my_recipes_data_cart'] = {}
    
    def __iter__(self):            
        my_recipes_list_id = self.my_recipes_cart_objects.keys()
        my_recipes = MyRecipes.objects.filter(id__in=my_recipes_list_id)
        my_recipes_data_temp = self.my_recipes_cart_objects.copy()
        for my_recipe in my_recipes:
            my_recipes_data_temp[str(my_recipe.id)]['my_recipe']=my_recipe
            # my_recipes_data_temp[str(my_recipe.id)]['my_recipe']={"id":my_recipe.id,"recipes_name":my_recipe.recipes_name,"recipes_price":my_recipe.recipes_price,"recipes_register_date":str(my_recipe.recipes_register_date),"recipes_user":my_recipe.recipes_user,"recipes_stuffs":my_recipe.recipes_stuffs.all(),"recipes_food":my_recipe.recipes_food}
        for item in my_recipes_data_temp.values():
            item['total_price']=int(item['final_price'])*item['qty']
            yield item
    
    def calc_total_price(self):
        sum=0
        for item in self.session.get('my_recipes_data_cart').values():
            sum+=(int(item['final_price'])*int(item['qty']))
        return sum