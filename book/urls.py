from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
	path("", views.book_list, name="list"),
	path("create/", views.book_create, name="create"),
	path("update/<int:book_id>/", views.book_update, name="update"),
	# path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]