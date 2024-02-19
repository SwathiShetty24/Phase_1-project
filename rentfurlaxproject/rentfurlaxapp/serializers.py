from rest_framework import serializers 
from .models import Register, Product, Category, Invoice

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Register
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ("__all__")
        
