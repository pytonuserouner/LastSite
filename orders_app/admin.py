from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdAt",
        "fullName",
        "email",
        "phone",
        "deliveryType",
        "paymentType",
        "totalCost",
        "status",
        "city",
        "address",
        "products",
    ]
