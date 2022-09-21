from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import user_view_set,book_view_set

router = routers.DefaultRouter()
router.register('users',user_view_set)
router.register('books',book_view_set)


urlpatterns = [
    path('', include(router.urls)),
]
