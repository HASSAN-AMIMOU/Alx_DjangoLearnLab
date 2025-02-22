# Retrieve Book Instance

## Command to Retrieve a Book:

```python
from bookshelf.models import Book

# Retrieve the book you just created
book = Book.objects.get(title="1984")

# Output the book instance
book
