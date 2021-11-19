
# from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from restapp import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"dishes", views.DishModelViewSet, basename="Dish")
router.register(r"categories", views.CategoryModelView, basename="Category")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name="obtain_auth_token"),
    # path('categories/', views.CategoryListAPIView.as_view(), name="categories"),
] + router.urls
