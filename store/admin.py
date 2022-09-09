from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page: int = 20
    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"

    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page: int = 20
    ordering = ["first_name", "last_name"]
 

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_per_page: int = 20


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "placed_at", "payment_status"]
    list_editable = ["payment_status"]
    list_per_page: int = 20
    ordering = ["id", "customer", "placed_at"]