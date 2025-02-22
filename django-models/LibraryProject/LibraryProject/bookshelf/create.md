# Create a Book Instance

## Command to Create a New Book:

```python
from bookshelf.models import Book

# Create a new book instance
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output the new book instance
new_book
