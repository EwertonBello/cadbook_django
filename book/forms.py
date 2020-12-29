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
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Páginas'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
        }
