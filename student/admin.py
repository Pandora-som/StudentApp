from django.contrib import admin

from .models import Students, Groups, Category, Product

admin.site.register(Students)
admin.site.register(Groups)

admin.site.register(Category)
admin.site.register(Product)