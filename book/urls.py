from django.urls import include, path

from . import views

app_name = "book"

urlpatterns = [
	path("api/v1/", include('book.api.v1.urls')),
	path("", views.book_dashboard, name="dashboard"),
	path("books/", views.book_list, name="list"),
	path("books/<int:book_id>/", views.book_detail, name="detail"),
	path("books/create/", views.book_create, name="create"),
	path("books/<int:book_id>/update/", views.book_update, name="update"),
	path("books/<int:book_id>/delete/", views.book_delete, name="delete"),
]