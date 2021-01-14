from django.db import models
from django.urls import reverse
from users.models import User

class BookManager(models.Manager):
    def create_book(self, title, user, price, pages):
        book = self.create(
            title=title,
            user=user,
            price=price,
            pages=pages,
        )
        return book

class Book(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pages = models.IntegerField()

    objects = BookManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book:detail", kwargs={"book_id": self.id})
