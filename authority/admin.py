from django.contrib import admin

from authority.models import BookTable

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('party_size','date', 'full_name','phone_number')
