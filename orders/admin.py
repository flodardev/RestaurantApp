from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import PizzaType, Topping, Sub, Pasta, Salad, DinnerPlatter, CustomerOrder, Pizza, Extra

# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/actions/
# Custom
admin.site.site_header = "Pinocchio's Admin Dashboard"

class CustomerOrderAdmin(admin.ModelAdmin):
    def make_delivering(self, request, queryset):
        updated = queryset.update(status="Delivering")
        self.message_user(request, ngettext(
            '%d order was successfully marked as "Delivering".', 
            '%d orders was successfully marked as "Delivering".', 
            updated,
            ) % updated, messages.SUCCESS)
    make_delivering.short_description = "Mark selected orders as delivering"

    def make_delivered(self, request, queryset):
        updated = queryset.update(status="Delivered")
        self.message_user(request, ngettext(
            '%d order was successfully marked as "Delivered".', 
            '%d orders was successfully marked as "Delivered".', 
            updated,
            ) % updated, messages.SUCCESS)
    make_delivered.short_description = "Mark selected orders as delivered"

    list_display = ('customer', 'item', 'name', 'size', 'price', 'topping1', 'topping2', 'topping3', 'extra1', 'extra2', 'extra3', 'status', 'date')
    list_filter = ('customer', 'status', 'date',)
    actions = [make_delivering, make_delivered]

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'small_price', 'large_price', 'topping_count')
    list_filter = ('name', 'menu')

class DinnerPlatterAdmin(admin.ModelAdmin):
    list_display = ('menu', 'small_price', 'large_price')
    list_filter = ('menu',)

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'small_price', 'large_price')
    list_filter = ('menu', 'name',)

class SaladAdmin(admin.ModelAdmin):
    list_display = ('menu', 'price')
    list_filter = ('menu',)

class PastaAdmin(admin.ModelAdmin):
    list_display = ('menu', 'price')
    list_filter = ('menu',)

class SubAdmin(admin.ModelAdmin):
    list_display = ('menu', 'extra_count', 'small_price', 'large_price')
    list_filter = ('menu',)

# Register your models here.
admin.site.register(PizzaType)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping)
admin.site.register(Sub, SubAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Salad, SaladAdmin)
admin.site.register(DinnerPlatter, DinnerPlatterAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(CustomerOrder, CustomerOrderAdmin)