from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import user_serializer,book_serializer
from .models import Book
# Create your views here.


class user_view_set(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer


class book_view_set(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = book_serializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]