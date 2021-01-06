from users.models import User
from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	pages = models.IntegerField()

	def __str__(self):
		return self.title
