from django.contrib import admin

from payment.models import BillingAddress

# Register your models here.
@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user','address','zip_code','city','country')
