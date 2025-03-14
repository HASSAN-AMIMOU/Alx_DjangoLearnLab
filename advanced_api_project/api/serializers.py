from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    - Serializes all fields of the Book model.
    - Includes custom validation to prevent future publication years.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation for publication_year.

        Ensures that the publication year is not set in the future.
        """
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    - Serializes the name field of the Author model.
    - Uses nested serialization to include books related to the author.
    - The books field is read-only, meaning books cannot be added/edited via this serializer.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    """
    Nested Serialization Explanation:

    - The `books` field uses the `BookSerializer` with `many=True` to handle multiple books.
    - `read_only=True` ensures that book records cannot be modified directly from the AuthorSerializer.
    - This enables automatic serialization of an author's books when retrieving author data.
    """
