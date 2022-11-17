from django.contrib import admin
from .models import Category, Product

# Register your models here.

# This 2 classes are created to put the informations in a tabular form. And onlyb the field listed will be seen in the table

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
