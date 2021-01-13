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

@pytest.fixture
def detail_response(client, book):
    return client.get(reverse("book:detail", kwargs={"book_id": book.id}))

@pytest.fixture
def create_response(client):
    return client.get(reverse("book:create"))

@pytest.fixture
def update_response(client, book):
    return client.get(reverse("book:update", kwargs={"book_id": book.id}))


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


class TestDetailView:
    def test_reverse_resolve(self, book):
        assert reverse("book:detail", kwargs={"book_id": book.id}) == f"/books/{book.id}/"
        assert resolve(f"/books/{book.id}/").view_name == "book:detail"

    def test_status_code(self, detail_response):
        assert detail_response.status_code == 200

    def test_template(self, detail_response):
        assertTemplateUsed(detail_response, "book/book_detail.html")


class TestCreateView:
    def test_reverse_resolve(self):
        assert reverse("book:create") == "/books/create/"
        assert resolve("/books/create/").view_name == "book:create"

    def test_status_code(self, create_response):
        assert create_response.status_code == 200

    def test_template(self, create_response):
        assertTemplateUsed(create_response, "book/book_form.html")


class TestUpdateView:
    def test_reverse_resolve(self, book):
        assert reverse("book:update", kwargs={"book_id": book.id}) == f"/books/{book.id}/update/"
        assert resolve(f"/books/{book.id}/update/").view_name == "book:update"

    def test_status_code(self, update_response):
        assert update_response.status_code == 200

    def test_template(self, update_response):
        assertTemplateUsed(update_response, "book/book_form.html")
