# Generated by Django 4.2.3 on 2023-07-26 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(blank=True, verbose_name="дата")),
                (
                    "fullName",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="полное имя"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="электронная почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="телефон"
                    ),
                ),
                (
                    "deliveryType",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="тип доставки"
                    ),
                ),
                (
                    "paymentType",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="тип оплаты"
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=11,
                        verbose_name="общая сумма",
                    ),
                ),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="статус"),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=255, verbose_name="город"),
                ),
                (
                    "address",
                    models.CharField(blank=True, max_length=255, verbose_name="адрес"),
                ),
                ("products", models.JSONField(blank=True, verbose_name="продукты")),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="заказы",
                        to="users_app.profile",
                    ),
                ),
            ],
        ),
    ]