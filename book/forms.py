from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = [
			'title',
			'user',
			'pages',
			'price',
		]
		labels = {
			'title': 'Título',
			'user': 'Autor',
			'pages': 'Páginas',
			'price': 'Preço',
		}
