# Generated by Django 4.2.3 on 2023-07-26 08:25

from django.db import migrations, models
import django.db.models.deletion
import products_app.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="название категории"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CategoryProduct",
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
                (
                    "title",
                    models.TextField(max_length=50, verbose_name="название категории"),
                ),
                (
                    "image",
                    models.FileField(blank=True, null=True, upload_to="uploads/"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Discount",
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
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, max_digits=3, verbose_name="скидка"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageCategory",
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
                (
                    "src",
                    models.ImageField(
                        blank=True,
                        upload_to=products_app.models.category_image_directory_path,
                        verbose_name="изображение категории",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="альтернатива картинке"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="цена"
                    ),
                ),
                ("count", models.IntegerField(default=0, verbose_name="количество")),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="название"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=2000, verbose_name="описание"
                    ),
                ),
                (
                    "fullDescription",
                    models.TextField(
                        blank=True, max_length=2000, verbose_name="описание"
                    ),
                ),
                (
                    "freeDelivery",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="бесплатная доставка?"
                    ),
                ),
                (
                    "reviews",
                    models.IntegerField(blank=True, verbose_name="количество обзоров"),
                ),
                (
                    "rating",
                    models.FloatField(blank=True, verbose_name="средний рейтинг"),
                ),
                (
                    "popular",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="популярный продукт"
                    ),
                ),
                (
                    "limited",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="осталось мало"
                    ),
                ),
                (
                    "discount",
                    models.IntegerField(
                        blank=True, default=None, verbose_name="скидка"
                    ),
                ),
                (
                    "discount_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=None,
                        max_digits=12,
                        verbose_name="цена со скидкой",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products_app.category",
                        verbose_name="категория",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "src",
                    models.ImageField(
                        blank=True,
                        upload_to=products_app.models.product_image_directory_path,
                        verbose_name="изображение продукта",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        blank=True, max_length=666, verbose_name="альтернатива картинке"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpecificationOfProduct",
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
                (
                    "name",
                    models.CharField(blank=True, max_length=128, verbose_name="size"),
                ),
                (
                    "value",
                    models.CharField(blank=True, max_length=128, verbose_name="value"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tags",
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
                (
                    "name",
                    models.CharField(blank=True, max_length=255, verbose_name="тег"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
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
                (
                    "author",
                    models.CharField(blank=True, max_length=255, verbose_name="автор"),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="электронная почта"
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True, max_length=4096, verbose_name="текст обзора"
                    ),
                ),
                (
                    "rate",
                    models.TextField(
                        blank=True, max_length=4096, verbose_name="оценка"
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, max_length=4096, verbose_name="дата"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review",
                        to="products_app.product",
                        verbose_name="название продукта",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="images",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products_app.productimage",
                verbose_name="изображения продукта",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="specifications",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="products_app.specificationofproduct",
                verbose_name="спецификация",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="products_app.tags",
                verbose_name="тэги",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products_app.imagecategory",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subcategories",
                to="products_app.category",
            ),
        ),
    ]