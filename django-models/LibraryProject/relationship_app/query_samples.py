import django
import os
from relationship_app.models import Author, Book, Library, Librarian

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace 'your_project' with your project name
django.setup()

# Query 1: All books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"Title: {book.title}, Author: {book.author.name}")

# Query 2: All books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the many-to-many relationship
    for book in books:
        print(f"Title: {book.title}")

# Query 3: Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")

# Sample Queries (Feel free to change the names to match actual data in your database)
print("Books by Author 'J.K. Rowling':")
books_by_author('J.K. Rowling')

print("\nBooks in 'Central Library':")
books_in_library('Central Library')

print("\nLibrarian for 'Central Library':")
librarian_for_library('Central Library')
