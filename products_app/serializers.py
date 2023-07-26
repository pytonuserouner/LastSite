from django.db.models import Avg
from rest_framework import serializers
from .models import (
    Product,
    Category,
    SpecificationOfProduct,
    Reviews,
    Tags,
    ProductImage,
    ImageCategory,
)


class CategoryImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = ImageCategory
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src


class CategoriesSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(method_name="get_image")
    subcategories = serializers.SerializerMethodField(method_name="get_subcategories")

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "images",
            "subcategories",
        )

    def get_subcategories(self, obj):
        subcategories = [
            {
                "id": obj.id,
                "title": obj.title,
                "image": {
                    "src": (obj.image or ""),
                    "alt": obj.title,
                },
            }
            for subcategory in obj.subcategories.all()
        ]
        return subcategories

    def get_image(self, obj):
        return {"src": (obj.image or ""), "alt": obj.title}


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["name"]


class SpecificationOfProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOfProduct
        fields = ["name", "value"]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            "author",
            "email",
            "text",
            "rate",
            "date",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField(method_name="get_scr")

    class Meta:
        model = ProductImage
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["category", "price", "count", "date",
                  "title", "description", "fullDescription", "freeDelivery",
                  "images", "tags", "reviews", "specifications", "rating",
                  "popular", "limited", "discount", "discount_price"]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer()
    tags = TagsSerializer()
    reviews = ReviewsSerializer()
    rating = serializers.SerializerMethodField(method_name="get_rating")
    salePrice = serializers.SerializerMethodField(method_name="get_sale_price")
    fullDescription = serializers.SerializerMethodField(
        method_name="get_full_description"
    )
    specifications = SpecificationOfProductSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "price",
            "salePrice",
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
        )
        extra_kwargs = {
            "freeDelivery": {"source": "free_delivery"},
            "description": {"source": "short_description"},
            "count": {"source": "quantity"},
        }

    def get_sale_price(self, obj):
        if not obj.discount:
            return None
        return round(obj.price - obj.price / 100 * obj.discount, 2)

    def get_full_description(self, obj):
        return obj.full_description

    def get_rating(self, obj):
        avg_rating = obj.reviews.aggregate(rating=Avg("rate"))
        return avg_rating["rating"]

# class ProductSerializer(serializers.ModelSerializer):
#     images = ProductImageSerializer()
#     tags = serializers.SerializerMethodField(method_name="get_tags")
#     reviews = serializers.SerializerMethodField(method_name="get_reviews")
#     rating = serializers.SerializerMethodField(method_name="get_rating")
#     salePrice = serializers.SerializerMethodField(method_name="get_sale_price")
#
#     class Meta:
#         model = Product
#         fields = (
#             "id",
#             "category",
#             "price",
#             "salePrice",
#             "count",
#             "date",
#             "title",
#             "description",
#             "freeDelivery",
#             "images",
#             "tags",
#             "reviews",
#             "rating",
#         )
#         extra_kwargs = {
#             "freeDelivery": {"source": "free_delivery"},
#             "description": {"source": "short_description"},
#             "count": {"source": "quantity"},
#         }
#
#     def get_tags(self, obj):
#         tags = [
#             {
#                 "id": tag.id,
#                 "name": tag.name,
#             }
#             for tag in obj.tags.all()
#         ]
#         return tags
#
#     def get_reviews(self, obj):
#         if not obj.reviews:
#             return 0
#         reviews = obj.reviews.count()
#         return reviews
#
#     def get_rating(self, obj):
#         avg_rating = obj.reviews.aggregate(rating=Avg("rate"))
#         return avg_rating["rating"]
#
#     def get_sale_price(self, obj):
#         if not obj.discount:
#             return None
#         return round(obj.price - obj.price / 100 * obj.discount, 2)
