from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
	path("books/", views.book_list, name="list"),
	path("books/<int:book_id>/", views.book_detail, name="detail"),
	path("books/create/", views.book_create, name="create"),
	path("books/update/<int:book_id>/", views.book_update, name="update"),
	# path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]