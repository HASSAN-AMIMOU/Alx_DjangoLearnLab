# Delete Book Instance

## Command to Delete a Book:

```python
from bookshelf.models import Book

# Retrieve the book you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify the deletion
book
