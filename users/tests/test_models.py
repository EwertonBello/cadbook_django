import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username="autor_test", email="autor@test.com"
    )
    assert user.username == "autor_test"
    assert user.email == "autor@test.com"
