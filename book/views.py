from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def book_dashboard(request):
    books = Book.objects.all()
    return render(request, 'book/book_dashboard.html', 
        {
        'books': books, 
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
        return redirect('book:list')
    return render(request, 'book/book_detail.html', {'book': book})

def book_create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book:list')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'book:list'}}">reload</a>""")
    else:
        return render(request, 'book/book_form.html', {'book_form':form, 'btn_submit': 'Cadastrar'})

def book_update(request, book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('book:list')
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
       form.save()
       return redirect('book:list')
    return render(request, 'book/book_form.html', {'book_form':form, 'btn_submit': 'Editar'})

def book_delete(request, book_id):
    if request.method == 'POST':
        book_id = int(book_id)
        try:
            book = Book.objects.get(id = book_id)
        except Book.DoesNotExist:
            return redirect('book:list')
        book.delete()
    return redirect('book:list')
