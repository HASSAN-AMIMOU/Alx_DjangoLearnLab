from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    
    Fields:
    - name: A string field to store the author's name.
    
    Relationships:
    - One-to-Many: One author can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.

    Fields:
    - title: A string field for the book title.
    - publication_year: An integer field for the year the book was published.

    Relationships:
    - A ForeignKey links each book to a single author (One-to-Many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title