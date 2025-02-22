from django.contrib import admin
from .models import Book

# Create a custom admin class
class BookAdmin(admin.ModelAdmin):
    # Customize the fields to display in the admin list view
    list_display = ('title', 'author', 'published_date')

    # Add filtering options in the admin
    list_filter = ('author',)

    # Add a search box to search by title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
