from django.shortcuts import render
from rest_framework import viewsets
#
from .models import *
from .serializers import *


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
