from django.shortcuts import render, redirect
from django.http import JsonResponse
from random import randrange
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users_app.models import *
from users_app.serializers import *
from products_app.models import *

User = get_user_model()
Profile = Profile.objects.all()
Products = Product.objects.all()

def banners(request):
    data = [
        {
            "id": Products.get(name=id),
            "category": Products.get(name="category"),
            "price": Products.get(name="price"),
            "count": Products.get(name="count"),
            "date": Products.get(name="date"),
            "title": Products.get(name="title"),
            "description": Products.get(name="description"),
            "freeDelivery": Products.get(name="freeDelivery"),
            "images": Products.get(name="images"),
            "tags": Products.get(name="tags"),
            "reviews": Products.get(name="reviews"),
            "rating": Products.get(name="ratings"),
        },
    ]
    return JsonResponse(data, safe=False)


def categories(request):
    data = [
        {
            "id": 123,
            "title": "video card",
            "image": {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "Image alt string",
            },
            "subcategories": [
                {
                    "id": 123,
                    "title": "video card",
                    "image": {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "Image alt string",
                    },
                }
            ],
        }
    ]
    return JsonResponse(data, safe=False)


def catalog(request):
    data = {
        "items": [
            {
                "id": Products.get(name='pk'),
                "category": Products.get(name="category"),
                "price": Products.get(name="price"),
                "count": Products.get(name="count"),
                "date": Products.get(name="date"),
                "title": Products.get(name="title"),
                "description": Products.get(name="description"),
                "freeDelivery": Products.get(name="freeDelivery"),
                "images": Products.get(name="images"),
                "tags": Products.get(name="tags"),
                "reviews": Products.get(name="reviews"),
                "rating": Products.get(name="rating"),
            }
        ],
        "currentPage": randrange(1, 4),
        "lastPage": 3,
    }
    return JsonResponse(data)


def productsPopular(request):
    data = [
        {
            "id": "123",
            "category": 55,
            "price": 500,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
                {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "hello alt",
                }
            ],
            "tags": [{"id": 0, "name": "Hello world"}],
            "reviews": 5,
            "rating": 4.6,
        }
    ]
    return JsonResponse(data, safe=False)


def productsLimited(request):
    data = [
        {
            "id": "123",
            "category": 55,
            "price": 500,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
                {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "hello alt",
                }
            ],
            "tags": [{"id": 0, "name": "Hello world"}],
            "reviews": 5,
            "rating": 4.6,
        }
    ]
    return JsonResponse(data, safe=False)


def sales(request):
    data = {
        "items": [
            {
                "id": 123,
                "price": 500,
                "salePrice": 200.67,
                "dateFrom": "05-08",
                "dateTo": "05-20",
                "title": "video card",
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
            }
        ],
        "currentPage": randrange(1, 4),
        "lastPage": 3,
    }
    return JsonResponse(data)


def basket(request):
    if request.method == "GET":
        print("[GET] /myapi/basket/")
        data = [
            {
                "id": 123,
                "category": 55,
                "price": 500,
                "count": 12,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            },
            {
                "id": 124,
                "category": 55,
                "price": 201.675,
                "count": 5,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            },
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        id = body["id"]
        count = body["count"]
        print(
            "[POST] /myapi/basket/   |   id: {id}, count: {count}".format(
                id=id, count=count
            )
        )
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500,
                "count": 13,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            }
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        body = json.loads(request.body)
        id = body["id"]
        print("[DELETE] /myapi/basket/")
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500,
                "count": 11,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            }
        ]
        return JsonResponse(data, safe=False)


def orders(request):
    if request.method == "POST":
        data = [
            {
                "id": 123,
                "category": 55,
                "price": 500,
                "count": 12,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            }
        ]
        return JsonResponse(data, safe=False)


def signIn(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body["username"]
        password = body["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)


def signUp(request):
    user_data = json.loads(request.body)
    user = User.objects.create_user(user_data.get("name"), user_data.get("email"), user_data.get("password"))
    # user = User.objects.create_user("mir232", "lennon@thebeatles.com", "pass232")
    user.save()
    return HttpResponse(status=200)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)


def product(request, id):
    data = {
        "id": 123,
        "category": 55,
        "price": 500,
        "count": 12,
        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        "title": "video card",
        "description": "description of the product",
        "fullDescription": "full description of the product",
        "freeDelivery": True,
        "images": [
            {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "hello alt",
            }
        ],
        "tags": [{"id": 0, "name": "Hello world"}],
        "reviews": [
            {
                "author": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "text": "rewrewrwerewrwerwerewrwerwer",
                "rate": 4,
                "date": "2023-05-05 12:12",
            }
        ],
        "specifications": [{"name": "Size", "value": "XL"}],
        "rating": 4.6,
    }
    return JsonResponse(data)


def tags(request):
    data = [
        {"id": 0, "name": "tag0"},
        {"id": 1, "name": "tag1"},
        {"id": 2, "name": "tag2"},
    ]
    return JsonResponse(data, safe=False)


def productReviews(request, id):
    data = [
        {
            "author": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "text": "rewrewrwerewrwerwerewrwerwer",
            "rate": 4,
            "date": "2023-05-05 12:12",
        },
        {
            "author": "2Annoying Orange",
            "email": "no-reply@mail.ru",
            "text": "rewrewrwerewrwerwerewrwerwer",
            "rate": 5,
            "date": "2023-05-05 12:12",
        },
    ]
    return JsonResponse(data, safe=False)


def profile(request):
    if request.method == "GET":
        data = {
            "fullName": Profile.objects.get("fullName"),  # "Annoying Orange",
            "email": Profile.objects.get("email"),  # "no-reply@mail.ru",
            "phone": Profile.objects.get('phone'),  # "88002000600",
            "avatar": {
                "src": Profile.objects.get("src"),
                "alt": Profile.objects.get("hello alt")  # "hello alt",
            },
        }
        with open("megano/getresponselog.txt", "w") as log:
            log.write(json.dumps(data))
        return JsonResponse(data)

    elif request.method == "POST":
        data = {
            "fullName": "Annoying Green",
            "email": "no-reply@mail.ru",
            "phone": "88002000600",
            "avatar": {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "hello alt",
            },
        }
        with open("megano/postresponselog.txt", "w") as log:
            log.write(json.dumps(data))
        return JsonResponse(data)

    return HttpResponse(status=500)


def profilePassword(request):
    return HttpResponse(status=200)


def orders(request):
    if request.method == "GET":
        data = [
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string",
                            }
                        ],
                        "tags": [{"id": 12, "name": "Gaming"}],
                        "reviews": 5,
                        "rating": 4.6,
                    }
                ],
            },
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string",
                            }
                        ],
                        "tags": [{"id": 12, "name": "Gaming"}],
                        "reviews": 5,
                        "rating": 4.6,
                    }
                ],
            },
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = {
            "orderId": 123,
        }
        return JsonResponse(data)

    return HttpResponse(status=500)


def order(request, id):
    if request.method == "GET":
        data = {
            "id": id,
            "createdAt": "2023-05-05 12:12",
            "fullName": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "phone": "88002000600",
            "deliveryType": "free",
            "paymentType": "online",
            "totalCost": 567.8,
            "status": "accepted",
            "city": "Moscow",
            "address": "red square 1",
            "products": [
                {
                    "id": 123,
                    "category": 55,
                    "price": 500.67,
                    "count": 12,
                    "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                    "title": "video card",
                    "description": "description of the product",
                    "freeDelivery": True,
                    "images": [
                        {
                            "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                            "alt": "Image alt string",
                        }
                    ],
                    "tags": [{"id": 12, "name": "Gaming"}],
                    "reviews": 5,
                    "rating": 4.6,
                },
            ],
        }
        return JsonResponse(data)

    elif request.method == "POST":
        data = {"orderId": 123}
        return JsonResponse(data)

    return HttpResponse(status=500)


def payment(request, id):
    print("qweqwewqeqwe", id)
    return HttpResponse(status=200)


def avatar(request):
    if request.method == "POST":
        # 		print(request.FILES["avatar"])
        return HttpResponse(status=200)
