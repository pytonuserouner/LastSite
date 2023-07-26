from django.urls import path, include
from rest_framework import routers

from .views import (
    BannersListApiView,
    CategoriesListApiView,
    CatalogListApiView,
    PopularListApiView,
    LimitedProductsApiView,
    ProductApiView,
    ReviewsProductApiView,
    TagsListApiView, CategoryProductView, ProductApiViewSet, IndexView,
)


name = "product_app"
app_label = "product_app"

# router = routers.DefaultRouter()
# router.register(r"catalog", ProductApiViewSet)


urlpatterns = [
    # path("", include((router.urls))),
    # path("catalog", include("rest_framework.urls", namespace="rest_framework")),
    # path("banners", IndexView.as_view(), name="banners"),
    path("banners", BannersListApiView.as_view(), name="banners"),
    path("categories", CategoryProductView.as_view(), name="categories"),
    # path("categories", CategoriesListApiView.as_view(), name="categories"),
    path("catalog", CatalogListApiView.as_view(), name="catalog"),
    path("products/popular", PopularListApiView.as_view(), name="popular"),
    path("products/limited", LimitedProductsApiView.as_view(), name="limited"),
    path("product/<int:id>", ProductApiView.as_view(), name="product"),
    path("product/<int:id>/reviews", ReviewsProductApiView.as_view(), name="review"),
    path("tags", TagsListApiView.as_view(), name="tags"),
]
