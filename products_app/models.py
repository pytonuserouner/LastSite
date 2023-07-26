from django.db import models

from diplastproject.settings import BASE_DIR


class SpecificationOfProduct(models.Model):
    """Model of specifications for products"""

    name = models.CharField(max_length=128, verbose_name="size", blank=True)
    value = models.CharField(max_length=128, verbose_name="value", blank=True)


def category_image_directory_path(instance: "Category", filename: str) -> str:
    return f"categories/category_{instance.pk}/image/{filename}"


class ImageCategory(models.Model):
    src = models.ImageField(
        blank=True,
        upload_to=BASE_DIR / 'uploads/categories/',
        # upload_to=category_image_directory_path,
        verbose_name="изображение категории",
    )
    alt = models.CharField(
        max_length=255, blank=True, verbose_name="альтернатива картинке"
    )


class CategoryProduct(models.Model):
    title = models.TextField(max_length=50, verbose_name="название категории")
    image = models.FileField(blank=True, null=True, upload_to="uploads/")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="название категории")
    image = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, blank=True)
    subcategory = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=True,
        related_name="subcategories",
        null=True,
    )


class Tags(models.Model):
    name = models.CharField(blank=True, max_length=255, verbose_name="тег")


class Product(models.Model):
    """Model of all products"""

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="категория"
    )
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="цена")
    count = models.IntegerField(verbose_name="количество", default=0)
    date = models.DateTimeField(
        blank=True, auto_now_add=True, verbose_name="дата создания"
    )
    title = models.CharField(
        null=True, blank=True, max_length=255, verbose_name="название"
    )
    description = models.TextField(blank=True, max_length=2000, verbose_name="описание")
    fullDescription = models.TextField(
        blank=True, max_length=2000, verbose_name="описание"
    )
    freeDelivery = models.BooleanField(
        blank=True, default=False, verbose_name="бесплатная доставка?"
    )
    images = models.ForeignKey(
        "ProductImage",
        on_delete=models.CASCADE,
        verbose_name="изображения продукта",
        blank=True,
    )
    tags = models.ForeignKey(
        "Tags", on_delete=models.PROTECT, verbose_name="тэги", blank=True
    )
    reviews = models.IntegerField(blank=True, verbose_name="количество обзоров")
    specifications = models.ForeignKey(
        SpecificationOfProduct,
        on_delete=models.PROTECT,
        verbose_name="спецификация",
        default=None,
        blank=True,
    )
    rating = models.FloatField(blank=True, verbose_name="средний рейтинг")
    popular = models.BooleanField(
        blank=True, default=False, verbose_name="популярный продукт"
    )
    limited = models.BooleanField(
        blank=True, default=False, verbose_name="осталось мало"
    )
    discount = models.IntegerField(blank=True, default=None, verbose_name="скидка")
    discount_price = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=12,
        default=None,
        verbose_name="цена со скидкой",
    )


def product_image_directory_path(instance: "Product", filename: str) -> str:
    """function for create path and save items of products images"""

    return f"products/product_{instance.pk}/image/{filename}"


class ProductImage(models.Model):
    """Model of products images"""

    src = models.ImageField(
        blank=True,
        upload_to=product_image_directory_path,
        verbose_name="изображение продукта",
    )
    alt = models.CharField(
        blank=True, max_length=666, verbose_name="альтернатива картинке"
    )


class Reviews(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="review",
        verbose_name="название продукта",
    )
    author = models.CharField(blank=True, max_length=255, verbose_name="автор")
    email = models.CharField(
        blank=True, max_length=255, verbose_name="электронная почта"
    )
    text = models.TextField(blank=True, max_length=4096, verbose_name="текст обзора")
    rate = models.TextField(blank=True, max_length=4096, verbose_name="оценка")
    date = models.DateTimeField(
        blank=True, auto_now_add=True, max_length=4096, verbose_name="дата"
    )


class Discount(models.Model):
    discount = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="скидка"
    )
