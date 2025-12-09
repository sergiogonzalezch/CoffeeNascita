from django.contrib import admin
from .models import MenuItem
# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ('name', 'price', 'in_menu', 'category', 'have_discount', 'discount_price')
    list_filter = ('in_menu', 'category', 'have_discount')
    search_fields = ('name', 'category__name')

admin.site.register(MenuItem, MenuItemAdmin)