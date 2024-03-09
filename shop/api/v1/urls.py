from django.urls import path

from shop.api.v1.views import CategoryViewList, SubCategoryViewDetail, ProductViewList, ImageViewList, ImageEditList

urlpatterns = [
    path('categories/', CategoryViewList.as_view(), name='category_list'),
    path('subcategories/<int:pk>', SubCategoryViewDetail.as_view(), name='subcategory_list'),
    path('products/', ProductViewList.as_view(), name='product_list'),
    path('images/', ImageViewList.as_view(), name='image_list'),
    path('images_edit/', ImageEditList.as_view(), name='image_edit')
]
