import factory
import factory.fuzzy

from ..models import Book
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText()
    email = factory.Faker("email")

    class Meta:
        model = User


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    user = factory.SubFactory(UserFactory)
    pages = factory.fuzzy.FuzzyInteger(1, 1000)
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)

    class Meta:
        model = Book
