# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="food_app"
urlpatterns = [ 
    # path('add-food/', add_food,name="add_food"),
    # path('delete-food/<int:id>/', delete_food,name="delete"),
    # path('edit-food/<int:id>/', edit_food,name="edit_food"),
    path('show-food/<str:slug>/',show_food,name="show_food"),
    path('show-food-part/',show_food_info,name="show_food_info"),
    path('show-foods/group/<str:group_id>/',show_foods_g,name="show_foods_width_group"),
    path('show-foods/',show_foods,name="show_foods"),
    path('show-similar-foods/',show_similar_foods,name="show_similar_foods"),
    
    path('add-to-my-recipes/',add_to_my_recipes,name="add_to_my_recipes"),
    path('update-my-recipe/',update_my_recipe,name="update_my_recipe"),
    path('delete-my-recipe/',delete_my_recipe,name="delete_my_recipe"),
    path('show-my-recipes/',show_my_recipes,name="show_my_recipes"),
    path('show-my-recipe/<int:recipe_id>/',show_my_recipe,name="show_my_recipe"),
    
    path('add-food-group/', add_food_group,name="add_food_group"),
    path('delete-food-group/', delete_food_group,name="delete_food_group"),
    path('edit-food-group/', edit_food_group,name="edit_food_group"),
    path('show-food-groups/',show_food_groups,name="show_food_groups"),
    
    path('add-recipes/',add_recipes,name="add_recipes"),
    path('delete-recipes/<int:id>/',delete_recipes,name="delete_recipes"),
    path('edit-recipes/',edit_recipes,name="edit_recipes"),
    path('show-recipe/<str:slug>/',show_recipes,name="show_recipe"),
    path('recipe/<int:id>/',show_recipe_with_id,name="show_recipe_with_id"),
    path('show-recipes/',show_all_recipes,name="show_recipes"),
    path('add-like-recipe/',add_like_recipe,name="add_like_recipe"),
    path('add-dislike-recipe/',add_dislike_recipe,name="add_dislike_recipe"),
    
    path('what',what_food,name="what_food"),
    
    path('show-comments/',show_comments,name="show_comments"),
]