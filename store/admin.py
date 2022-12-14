from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from . import models




# Register your models here.



class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name: str = "inventory"

    def lookups(self, request, model_admin):
        return [
            ("<10", "Low"),
            ("0", "None") 
        ]
    
    def queryset(self, request, queryset):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)
        if self.value() == "0":
            return queryset.filter(inventory__lte=0)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ["thumbnail"]

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ""


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    autocomplete_fields = ["collection"]
    prepopulated_fields = {
        "slug": ["title"]
    }
    actions = ["clear_inventory"]
    inlines = [ProductImageInline]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page: int = 20
    list_select_related = ["collection"]
    list_filter = ["collection", "last_update", InventoryFilter]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            if product.inventory <= 0:
                return "None"
            return "Low"
        return "OK"

    def collection_title(self, product):
        return product.collection.title

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products were successfully updated.",
            messages.SUCCESS
        )
    
    class Media:
        css = {
            "all": ["store/styles.css"]
        }


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name"]
    list_display = ["first_name", "last_name", "membership", "orders_count"]
    list_editable = ["membership"]
    list_per_page: int = 20
    list_select_related = ["user"]
    ordering = ["user__first_name", "user__last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]

    @admin.display(ordering="orders_count")
    def orders_count(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({
                "customer_id": str(customer.id),
        }))
        return format_html("<a href='{}'>{} Orders</a>", url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .annotate(orders_count= Count("order"))


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "products_count"]
    list_per_page: int = 20

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({
                "collection__id": str(collection.id),
            }))
        return format_html("<a href='{}'>{}</a>", url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .annotate(products_count=Count("products"))


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ["product"]
    model = models.OrderItem
    min_num = 1
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    autocomplete_fields = ["customer"]
    list_display = ["id", "customer", "placed_at", "payment_status"]
    list_editable = ["payment_status"]
    list_per_page: int = 20
    ordering = ["id", "customer", "placed_at"]