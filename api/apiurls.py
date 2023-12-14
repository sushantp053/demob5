from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"students", views.StudentViewSet)
router.register(r"departments", views.DepartmentViewSet)


urlpatterns = [
    path("demoapi", views.demoapi),
    path("", include(router.urls)),
]
