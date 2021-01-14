import pytest
from pytest_django.asserts import assertQuerysetEqual

from ..models import Book

pytestmark = pytest.mark.django_db


class TestBookModel:
    def test___str__(self, book):
        assert book.__str__() == book.title
        assert str(book) == book.title

    def test_get_absolute_url(self, book):
        url = book.get_absolute_url()
        assert url == f"/books/{book.id}/"

    def test_create_book(self, user):
        book = Book.objects.create_book(
            title="book test",
            user=user,
            price=99.90,
            pages=25
        )
        assert book.title == "book test"
        assert book.user == user
        assert book.price == 99.90
        assert book.pages == 25
