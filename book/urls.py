from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
	path("books/", views.book_list, name="list"),
	path("books/<int:book_id>/", views.book_detail, name="detail"),
	path("books/create/", views.book_create, name="create"),
	path("books/<int:book_id>/update", views.book_update, name="update"),
	path("books/<int:book_id>/delete", views.book_delete, name="delete"),
]