from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'category', 'price', 'quantity', 'discount', 'cod')
    search_fields = ('title', 'desc', 'price')
    list_filter = ('category', 'cod', 'user')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# customizing admin panel's title and name
admin.site.site_title = 'Ecom' # Page title
admin.site.site_header = 'ECOM' # Brand Name
admin.site.index_title = 'Admin Panel' # Panel Name