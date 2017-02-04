from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search(request):
    errors = []
    
    if 'q' in request.GET:
        try: q = request.GET['q']
        except: pass

        if not q:
            errors.append('Pleae enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q).order_by('-publication_date')
            return render(request, 'search.html', {'books': books, 'query': q})
        
    return render(request, 'search.html', {'errors': errors})