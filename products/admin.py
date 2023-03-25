from django.contrib import admin

# models
from products.models import FoodCategories
from products.models import MenuFood
from products.models import Foods



@admin.register(FoodCategories)
class FoodCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name','created_at','modified_at')
    search_fields = ('category_name',)
    list_per_page = 50

@admin.register(MenuFood)
class SetMenuFoodAdmin(admin.ModelAdmin):
    list_display = ('food_name','created_at','modified_at','is_active')
    search_fields = ('food_name',)
    list_filter = ('is_active',)
    list_per_page = 50

@admin.register(Foods)
class SetMenuAdmin(admin.ModelAdmin):
    list_display=('menu_name','menu_id','price','offer_percentage','new_price')
    search_fields =('menu_name',)
    list_filter = ('is_active',)
    list_per_page = 50
