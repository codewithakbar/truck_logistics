from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if "price" in representation:
            representation["price"] = f"{representation['price']:,}".replace(",", " ")

        return representation