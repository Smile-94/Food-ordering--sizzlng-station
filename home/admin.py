from django.contrib import admin

# models
from home.models import CustomerMessage

# Register your models here.
@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email')
    list_per_page =50

