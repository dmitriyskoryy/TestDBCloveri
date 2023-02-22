from django.contrib import admin
from .models import *
# Register your models here.


class CategoryMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
class UsersOrderAdmin(admin.ModelAdmin):
    list_display = ('user',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_order', 'name_product')


admin.site.register(CategoryMenu, CategoryMenuAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UsersOrder, UsersOrderAdmin)
admin.site.register(Order, OrderAdmin)