from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from books.models import Book
from django.core.mail import send_mail


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
    
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'), ['brandon.jaus@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})