from itertools import count
from typing import Counter
from django.contrib import admin
from . import models

@admin.register(models.Product)  # with this we no more need for this admin.site.register(models.Product,ProductAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','unit_price','invenory_status','collection_title']
    list_editable=['unit_price']
    list_per_page=10
    list_select_related=['collection']
    def collection_title(self,product):
        return product.collection.title 
    @admin.display(ordering='inventory')
    def invenory_status(self,product):
        if product.inventory<10:
            return 'Low'
        return 'Ok'
    # for list of this google for modellist admin 
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','products_count']
    
    def products_count(self,collection):
        return collection.products_count
    
    def get_queryset(self,request):
        return  super().get_queryset(request).annotate(
            products_count=count('product')
        )

# admin.site.register(models.Product,ProductAdmin)
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','membership']
    list_editable=['membership']
    ordering=['first_name','last_name']
    list_per_page=10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','placed_at','customer']

# Register your models here.
