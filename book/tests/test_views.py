import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db

@pytest.fixture
def dashboard_response(client):
    return client.get(reverse("book:dashboard"))

@pytest.fixture
def list_response(client):
    return client.get(reverse("book:list"))


class TestDashboardView:
    def test_reverse_resolve(self):
        assert reverse("book:dashboard") == "/"
        assert resolve("/").view_name == "book:dashboard"

    def test_status_code(self, dashboard_response):
        assert dashboard_response.status_code == 200

    def test_template(self, dashboard_response):
        assertTemplateUsed(dashboard_response, "book/book_dashboard.html")


class TestListView:
    def test_reverse_resolve(self):
        assert reverse("book:list") == "/books/"
        assert resolve("/books/").view_name == "book:list"

    def test_status_code(self, list_response):
        assert list_response.status_code == 200

    def test_template(self, list_response):
        assertTemplateUsed(list_response, "book/book_list.html")
