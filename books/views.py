from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search(request):
    error = False
    q = None
    
    if 'q' in request.GET:
        q = request.GET['q']
    
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q).order_by('-publication_date')
            return render(request, 'search.html', {'books': books, 'query': q})
    
    return render(request, 'search.html', {'error': error})