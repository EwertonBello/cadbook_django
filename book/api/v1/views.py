from rest_framework import viewsets
from book.models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows books to be viewed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
