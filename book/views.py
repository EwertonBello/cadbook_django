from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES,
            initial={'btn_title': 'Cadastrar'}
        )
        if form.is_valid():
            form.save()
            return redirect('book:list')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'book:list'}}">reload</a>""")
    else:
        return render(request, 'book/book_form.html', {'book_form':form})

def book_update(request, book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('book:list')
    form = BookForm(request.POST or None, instance = book, 
        initial={'btn_title': 'Alterar'}
    )
    if form.is_valid():
       form.save()
       return redirect('book:list')
    return render(request, 'book/book_form.html', {'book_form':form})

def book_delete(request, book_id):
    pass
    # book_id = int(book_id)
    # try:
    #     book_sel = Book.objects.get(id = book_id)
    # except Book.DoesNotExist:
    #     return redirect('book:list')
    # book_sel.delete()
    # return redirect('book:list')
