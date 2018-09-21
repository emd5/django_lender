from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Book


def books_list_view(request):
    """This function check user credentials and displays the books of the right user"""
    if not request.user.is_authenticated:
        raise PermissionDenied

    books = Book.objects.filter(user__username=request.user.username)

    context = {
        'books': books
    }

    return render(request, 'books/book_list.html', context=context)


def books_detail_view(request, pk=None):
    """This function checks credentials of user associated to the book details page"""
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    book = get_object_or_404(Book, id=pk, user__id=request.user.id)
    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
