from django.contrib import admin


# models
from authority.models import FoodCategories

@admin.register(FoodCategories)
class FoodCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name','created_at','modified_at')
    search_fields = ('category_name',)
    list_per_page = 50