from django.contrib import admin
from .models import MenuItem, Order, OrderMenuItem


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = (
        "name",
        "price",
        "in_menu",
        "category",
        "have_discount",
        "discount_price",
    )
    list_filter = ("in_menu", "category", "have_discount")
    search_fields = ("name", "category__name")


class OrderMenuItemInline(admin.TabularInline):
    model = OrderMenuItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderMenuItemInline]


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
