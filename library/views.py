from django.shortcuts import render, redirect
from .models import Library, Book, Column, Shelf, Group, Author
from .forms import BookForm, ColumnForm, ShelfForm, GroupForm, LibraryForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Library, Book, Column, Shelf, Group, Author

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'library_detail.html', {'library': library})

def genre_detail(request, genre):
    books = Book.objects.filter(genre__iexact=genre)
    return render(request, 'genre_detail.html', {'genre': genre, 'books': books})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    other_books = Book.objects.filter(author=book.author).exclude(pk=pk)
    context = {
        'book': book,
        'other_books': other_books
    }
    return render(request, 'book_detail.html', context)

def landing_page(request):
    search_query = request.GET.get('search', '')
    libraries = Library.objects.filter(name__icontains=search_query)
    genres = Book.objects.filter(genre__icontains=search_query).values_list('genre', flat=True).distinct()
    authors = Author.objects.filter(name__icontains=search_query)
    books = Book.objects.filter(title__icontains=search_query)

    context = {
        'libraries': libraries,
        'genres': genres,
        'authors': authors,
        'books': books,
        'search_query': search_query,
    }
    return render(request, 'landing_page.html', context)


def submit_item(request):
    if request.method == 'POST':
        item_type = request.POST.get('item_type')
        if item_type == 'book':
            form = BookForm(request.POST)
        elif item_type == 'column':
            form = ColumnForm(request.POST)
        elif item_type == 'shelf':
            form = ShelfForm(request.POST)
        elif item_type == 'group':
            form = GroupForm(request.POST)
        elif item_type == 'library':
            form = LibraryForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            form.save()
            messages.success(request, 'Item submitted successfully!')
            return redirect('submit_item')
    else:
        form = None

    return render(request, 'submit_item.html', {'form': form})

def get_form_fields(request, item_type):
    if item_type == 'book':
        form = BookForm()
    elif item_type == 'column':
        form = ColumnForm()
    elif item_type == 'shelf':
        form = ShelfForm()
    elif item_type == 'group':
        form = GroupForm()
    elif item_type == 'library':
        form = LibraryForm()
    else:
        form = None

    if form:
        return render(request, 'includes/form_fields.html', {'form': form})
    else:
        return render(request, 'includes/form_fields.html')

