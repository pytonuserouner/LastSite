from django.db import models

from products_app.models import Product
from users_app.models import Profile



class Order(models.Model):
    DELIVERY_CHOICES = [
        ("free", "free delivery"),
        ("express", "paid delivery"),
    ]
    PAYMENT_CHOICES = [("online", "online payment"), ("offline", "offline payment")]
    STATUS_CHOICES = [
        ("accepted", "accepted order"),
        ("rejected", "rejected order"),
        ("delivery", "order on delivery"),
        ("delivered", "order is already delivered"),
    ]

    createdAt = models.DateTimeField(blank=True, verbose_name="дата")
    fullName = models.CharField(blank=True, max_length=255, verbose_name="полное имя")
    email = models.CharField(
        blank=True, max_length=255, verbose_name="электронная почта"
    )
    phone = models.CharField(blank=True, max_length=255, verbose_name="телефон")
    deliveryType = models.CharField(
        blank=True, max_length=255, verbose_name="тип доставки"
    )
    paymentType = models.CharField(
        blank=True, max_length=255, verbose_name="тип оплаты"
    )
    totalCost = models.DecimalField(
        blank=True, decimal_places=2, max_digits=11, verbose_name="общая сумма"
    )
    status = models.CharField(blank=True, max_length=255, verbose_name="статус")
    city = models.CharField(blank=True, max_length=255, verbose_name="город")
    address = models.CharField(blank=True, max_length=255, verbose_name="адрес")
    products = models.JSONField(verbose_name="продукты", blank=True)
    user = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="заказы", default=None
    )

    def __str__(self):
        return f"Order: {self.id}"
