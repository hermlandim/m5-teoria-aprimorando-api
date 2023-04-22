from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class ListBookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
