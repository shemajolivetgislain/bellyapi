from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from restapp.models import Category, Dish
from restapp.serializers import CategorySerializer, ReadDishSerializer, WriteDishSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


class CategoryModelView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    pagination_class = None

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class DishModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("description", "names")
    filterset_fields = ("category__name",)

    def get_queryset(self):
        return Dish.objects.select_related("category", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "Retrieve"):
            return ReadDishSerializer
        return WriteDishSerializer



