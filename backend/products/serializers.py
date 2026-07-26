from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    def validate_name(self,value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("product name must cantain 3 characters")
        return value
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("price should be greater then zero")
        return value
    def validate_discount(self,value):
        if value <0 or value > 100:
            raise serializers.ValidationError("discount must be between 0 and 100")
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock cannot be negative."
            )
        return value

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 0 and 5."
            )
        return value
    def validate(self, data):
       if data.get("is_featured") and data.get("rating", 0) < 4:
        raise serializers.ValidationError({
            "rating": "Featured products must have a rating of at least 4.0."
        })

       if data.get("discount", 0) > 0 and data.get("price", 0) <= 100:
        raise serializers.ValidationError({
            "price": "Discounted products must have a price greater than 100."
        })

       return data
    class Meta:
        model = Product
        fields = "__all__"