from django.contrib import admin

from .models import Students, Groups

admin.site.register(Students)
admin.site.register(Groups)

# admin.site.register(Category)
# admin.site.register(Product)