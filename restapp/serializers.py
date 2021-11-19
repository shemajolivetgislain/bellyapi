from django.contrib.auth.models import User
from rest_framework import serializers
from restapp.models import Dish, Category


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
        read_only_fields = fields


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ("id", "name", "user")


class WriteDishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dish
        fields = (
            "user",
            "names",
            "image",
            "price",
            "description",
            "category"
        )


def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    user = self.context["request"].user
    self.fields["category"].queryset = user.categories.all()


class ReadDishSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Dish
        fields = (
            "id",
            "names",
            "image",
            "price",
            "description",
            "category",
            "user"
        )
        read_only_fields = fields
