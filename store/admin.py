from itertools import count
from typing import Any, Counter
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.db.models import Count


from tags.models import TaggedItem
from . import models


# with this we no more need for this admin.site.register(models.Product,ProductAdmin)
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields=['collection']
    # inlines=[TagInline]
    prepopulated_fields={
        'slug':['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price',
                    'invenory_status', 'collection_title']
    list_filter = ['collection', 'last_update']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title','quantity','unit_price']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def invenory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    # for list of this google for modellist admin

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f'{updated_count} Products were successfully updated', messages.ERROR)


@ admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields=['title']
    @ admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

# admin.site.register(models.Product,ProductAdmin)


@ admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

class OrderItemline(admin.TabularInline):
    autocomplete_fields=['product']
    model=models.OrderItem
    extra=0
@ admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    inlines=[OrderItemline]
    autocomplete_fields=['customer']
# Register your models here.
