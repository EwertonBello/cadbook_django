from book.models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'user',
            'pages',
            'price',
        ]
