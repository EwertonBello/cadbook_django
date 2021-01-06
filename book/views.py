from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from users.models import User

from .forms import BookForm
from .models import Book

def book_dashboard(request):
    books = Book.objects.all()
    widget = {
        'books': Book.objects.count(),
        'total_price': Book.objects.aggregate(total_price=Sum('price'))['total_price'],
        'users': User.objects.count(),
        'total_pages': Book.objects.aggregate(total_pages=Sum('pages'))['total_pages']
    }
    return render(request, 'book/book_dashboard.html', 
        {
        'widget': widget, 
        'current_path': request.get_full_path()
        }
    )

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', 
        {
        'books': books, 
        'current_path': request.get_full_path()
        }
    )

def book_detail(request, book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        messages.error(request, "Livro não existe!" )
        return redirect('book:list')
    return render(request, 'book/book_detail.html', {'book': book})

def book_create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro cadastrado com sucesso!" )
            return redirect('book:list')
    return render(request, 'book/book_form.html', {'book_form':form, 'btn_submit': 'Cadastrar'})

def book_update(request, book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        messages.error(request, "Livro não existe!" )
        return redirect('book:list')
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
       form.save()
       messages.info(request, "Livro alterado com sucesso!" )
       return redirect('book:list')
    return render(request, 'book/book_form.html', {'book_form':form, 'btn_submit': 'Editar'})

def book_delete(request, book_id):
    if request.method == 'POST':
        book_id = int(book_id)
        try:
            book = Book.objects.get(id = book_id)
        except Book.DoesNotExist:
            messages.error(request, "Livro não existe!" )
            return redirect('book:list')
        book.delete()
    return JsonResponse({'message': "Exclusão bem sucedida!"})
