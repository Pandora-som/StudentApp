from django.contrib import admin

from .models import Students, Groups, Status

admin.site.register(Students)
admin.site.register(Groups)
admin.site.register(Status)

# admin.site.register(Category)
# admin.site.register(Product)