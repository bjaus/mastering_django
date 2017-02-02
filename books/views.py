from django.shortcuts import render


def search_form(request):
    return render(request, 'search_form.html')


# def display_meta(request):
    # values = request.META.items()
    # values.sort()
    # html = []
    # for k, v in values:
        # html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, v))
    # return HttpResponse('<table>{}</table>'.format(html))
    
# git issue test