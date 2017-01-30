from rest_framework import serializers
from store.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'parent_category', 'cover', 'description')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    class Meta:
        model = VendorProduct
        fields = ('product', 'vendor', 'price', 'price_rule')

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('id', 'vendor', 'client', 'phone_number', 'alter_phone_number', 'shipping_address',
                  'city', 'province', 'country', 'post_code', 'comment', 'shipping_fee', 'total_price',
                  'status', 'status_description')
