from django.contrib import admin


# models
from authority.models import FoodCategories
from authority.models import SetMenuFood
from authority.models import SetMenu
from authority.models import BookTable

@admin.register(FoodCategories)
class FoodCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name','created_at','modified_at')
    search_fields = ('category_name',)
    list_per_page = 50

@admin.register(SetMenuFood)
class SetMenuFoodAdmin(admin.ModelAdmin):
    list_display = ('food_name','created_at','modified_at','is_active')
    search_fields = ('food_name',)
    list_filter = ('is_active',)
    list_per_page = 50

@admin.register(SetMenu)
class SetMenuAdmin(admin.ModelAdmin):
    list_display=('menu_name','menu_id','price','offer_percentage','new_price')
    search_fields =('menu_name',)
    list_filter = ('is_active',)
    list_per_page = 50

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('party_size','date', 'full_name','phone_number')
