from rest_framework import serializers

from .models import Order


class OrdersSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(method_name="get_createdAt")
    fullName = serializers.SerializerMethodField(method_name="get_fullName")
    email = serializers.SerializerMethodField(method_name="get_email")
    phone = serializers.SerializerMethodField(method_name="get_phone")
    deliveryType = serializers.SerializerMethodField(method_name="get_deliveryType")
    paymentType = serializers.SerializerMethodField(method_name="get_paymentType")
    totalCost = serializers.SerializerMethodField(method_name="get_totalCost")

    class Meta:
        model = Order
        fields = (
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
        )

    def get_createdAt(self, obj):
        return obj.created_at

    def get_fullName(self, obj):
        return obj.user.profile.fullName

    def get_email(self, obj):
        return obj.user.profile.email

    def get_phone(self, obj):
        return str(obj.user.profile.phone)

    def get_deliveryType(self, obj):
        return obj.delivery_type

    def get_paymentType(self, obj):
        return obj.payment_type

    def get_totalCost(self, obj):
        return obj.total_cost
