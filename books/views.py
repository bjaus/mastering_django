from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search_form(request):
    return render(request, 'search_form.html')

    
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q).order_by('-publication_date')
        return render(request, 'search_result.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')