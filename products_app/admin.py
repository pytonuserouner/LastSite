from django.contrib import admin

from products_app.models import (
    SpecificationOfProduct,
    Product,
    Tags,
    Reviews,
    ProductImage,
    Category,
    ImageCategory,
)


@admin.register(SpecificationOfProduct)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]

    class Meta:
        verbose_name = "Спецификация"


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["src", "alt"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category",
        "price",
        "count",
        "date",
        "title",
        "description",
        "fullDescription",
        "freeDelivery",
        "images",
        "tags",
        "reviews",
        "specifications",
        "rating",
    ]


@admin.register(ImageCategory)
class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ["src", "alt"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author",)
