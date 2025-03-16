from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend 



class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


class BookListView(generics.ListAPIView):

    """Handles listing all books"""
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

class BookCreateView(generics.CreateAPIView):

    """Handles creating a new book"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  

class BookDetailView(generics.RetrieveAPIView):

    """Handles retrieving a single book by ID"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class BookUpdateView(generics.UpdateAPIView):
    """Handles updating an existing book"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  

class BookDeleteView(generics.DestroyAPIView):

    """Handles deleting a book"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  
