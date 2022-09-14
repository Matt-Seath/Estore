from rest_framework import serializers
from decimal import Decimal
from .models import *


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "slug", "inventory", "price", "price_with_tax", "collection"]

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source="unit_price")
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return round(product.unit_price * Decimal(1.1), 2)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "created_at"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.price = validated_data.get("price")
    #     instance.save()
    #     return instance