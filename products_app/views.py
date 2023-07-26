from typing import Iterable, Dict

from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Reviews, Category, Tags, CategoryProduct
from .serializers import (
    ProductDetailSerializer,
    ProductSerializer,
    ReviewsSerializer,
    CategoriesSerializer,
    TagsSerializer,
)


class CategoryProductView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        categories_serialized_data = []
        for category in categories:
            categories_serialized_data.append(
                {
                    "id": str(category.id),
                    "title": category.title,
                    "image": {
                        "scr": str(category.image),
                        "alt": "hello alt",
                    },
                    "href": "/catalog/" + str(category.id),
                    "subcategories": [
                        {
                            "id": str(category.id),
                            "title": category.title,
                            "image": {
                                "scr": str(category.image),
                                "alt": "hello alt",
                            },
                            "href": "/catalog/" + str(category.id)}
                    ]
                }
            )
        return JsonResponse(categories_serialized_data, safe=False)


class CategoriesListApiView(ListAPIView):
    """Список категорий"""

    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CatalogListApiView(ListAPIView):
    """Каталог"""

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.query_params:
            name = self.request.query_params.get("filter[name]")
            if name:
                queryset = queryset.filter(description__icontains=name)

            min_price = self.request.query_params.get("filter[minPrice]")
            if min_price:
                queryset = queryset.filter(description__icontains=min_price)

            max_price = self.request.query_params.get("filter[maxPrice]")
            if max_price:
                queryset = queryset.filter(description__icontains=max_price)

            free_delivery = self.request.query_params.get("filter[freeDelivery]")
            if free_delivery:
                queryset = queryset.filter(description__icontains=free_delivery)

            available = self.request.query_params.get("filter[available]")
            if available:
                queryset = queryset.filter(description__icontains=available)


class PopularListApiView(ListAPIView):
    """Список популярных товаров"""

    queryset = Product.objects.prefetch_related("popular")
    serializer_class = ProductSerializer


class LimitedProductsApiView(ListAPIView):
    """Список товаров, которых мало осталось"""

    queryset = Product.objects.prefetch_related("limited")[:5]
    serializer_class = ProductSerializer


class SalesListApiView(ListAPIView):
    """Список товаров со скидкой"""

    queryset = Product.objects.prefetch_related("discount").filter(discount__gt=0)
    serializer_class = ProductSerializer


class BannersListApiView(ListAPIView):
    """Товары для баннеров на главной"""

    queryset = Product.objects.all()[:5]
    serializer_class = ProductSerializer


class TagsListApiView(ListAPIView):
    "Список тэгов"

    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductApiView(RetrieveAPIView):
    """Подробное описание продукта"""

    serializer_class = ProductDetailSerializer
    queryset = Product.objects.prefetch_related("images").all()


class ReviewsProductApiView(APIView):
    """Список обзоров на продукты"""

    def post(self, request, pk, *args, **kwargs):
        serializer = ReviewsSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            review = Reviews(
                product=Product.objects.get(id=pk),
                author=self.request.user,
                rate=serializer.data.get("rate"),
                text=serializer.data.get("text"),
            )
            review.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndexView(ListView):
    """
    Главная страница

    ::Страница: Главная
    """
    model = Product
    template_name = 'frontend/index.html'
    context_object_name = 'products'

    def get_queryset(self) -> Iterable:
        products = Product.objects.all()
        return products

    def get_context_data(self, **kwargs) -> Dict:
        limited_products = Product.objects.all()
        context = {
            'banners': Product.objects.all(),
            'limited_products': Product.objects.all(),
            'hot_offers': Product.objects.all(),
            'random_categories': Product.objects.all()}
        return context


