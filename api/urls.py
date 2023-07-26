from django.urls import path
from .views import *

name = "api"
app_label = "api"

urlpatterns = [
    path("banners", banners),
    path("categories", categories),
    path("catalog", catalog),
    path("products/popular", productsPopular),
    path("products/limited", productsLimited),
    path("product/<int:id>", product),
    path("product/<int:id>/reviews", productReviews),
    path("tags", tags),
    path("sales", sales),
    path("basket", basket),
    path("orders", orders),
    path("order/<int:id>", order),
    path("payment/<int:id>", payment),
    path("sign-in", signIn),
    path("sign-up", signUp),
    path("sign-out", signOut),
    path("profile", profile),
    path("profile/password", profilePassword),
    path("profile/avatar", avatar),
]
