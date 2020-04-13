from rest_framework import serializers
from .models import User,Address,Order,Receipt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        mooel = Address
        fields=["__all__"]
    
class OrderSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Order
        fields=["__all__"]
    
class ReceiptSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    order = OrderSerializer()
    class Meta:
        model = Receipt
        fields=["__all__"]
        
