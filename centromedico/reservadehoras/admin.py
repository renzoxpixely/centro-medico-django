from django.contrib import admin



from .models import Category
from .models import Product
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
         list_display = ('name','slug')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
         list_display = ('name','name','name')

admin.site.register(Product, ProductAdmin)


