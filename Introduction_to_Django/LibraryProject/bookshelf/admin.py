# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the fields to display in the admin list view
    list_display = ('title', 'author', 'published_date')

    # Add a filter to filter by publication year (using 'published_date__year')
    list_filter = ('author', 'published_date__year')  # This will filter by year

    # Add a search box to search by title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
