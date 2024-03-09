from rest_framework import generics
from shop.api.v1.serializers import CategorySerializer,SubCategorySerializer,ProductSerializer,ImagesSerializer,ImageEditSerializer
from shop.models import Category,SubCategory,Product,Images,ImageEdit


class CategoryViewList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewDetail(generics.ListAPIView):
    queryset = SubCategory.objects.prefetch_related('category').all()
    serializer_class = SubCategorySerializer

class ProductViewList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageViewList(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class ImageEditList(generics.ListAPIView):
    queryset = ImageEdit.objects.all()
    serializer_class = ImageEditSerializer



