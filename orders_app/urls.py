from django.urls import path

from orders_app.views import CartAPIView

urlpatterns = [
    path("basket", CartAPIView.as_view(), name="basket"),
]
