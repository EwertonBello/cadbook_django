import pytest

from book.tests.factories import UserFactory, BookFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def book():
    return BookFactory()