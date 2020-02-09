from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display= ['title','__str__','price','timestamp']
    list_editable = ['price']
    list_filter =  ['price', 'active']
    readonly_fields = ['update','timestamp']
    search_fields= ['title','price','timestamp','description']
    prepopulated_fields = {"slug" :('title',)}
    
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)




