from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library



def list_books(request):
    # Query all books from the database
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'