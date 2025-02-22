# Update Book Instance

## Command to Update a Book:

```python
from bookshelf.models import Book

# Retrieve the book you created earlier
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Output the updated book
book
