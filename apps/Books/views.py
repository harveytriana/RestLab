# ------------------------------------
# * Books.views *
# ------------------------------------
from django.shortcuts import render
from rest_framework import viewsets
#
from .models import *
from .serializers import *
#
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# API View (another approach)
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Learming ViewSets
# ------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/viewsets/
class LEARNING_BookViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Books.
    """
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

# APIView Sample
class BookTitles(APIView):
    """
    Returns the list of titles in the database
    """
    def get(self, request, format=None):
        return  Response([b.Title for b in Book.objects.all().order_by('Title')])
