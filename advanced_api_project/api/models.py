from django.db import models

class Author(models.Model):
    """
    Model representing an author.

    Fields:
    - name: Stores the author's name as a string.
    
    Relationships:
    - An author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.

    Fields:
    - title: Stores the book's title as a string.
    - publication_year: Stores the year the book was published as an integer.
    
    Relationships:
    - Each book is associated with a single author via a ForeignKey.
    - The 'related_name' attribute allows reverse lookup from Author to Books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
