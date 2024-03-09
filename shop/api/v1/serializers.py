from rest_framework import serializers

from shop.models import Category, SubCategory, Product, Images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', 'created_at']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ImageEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
