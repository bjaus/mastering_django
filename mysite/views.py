from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

    
def current_datetime(request):
    now = datetime.datetime.now()
    return render(
        request, 
        'current_datetime.html', 
        {'current_datetime': now}
    )
    
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError as ve:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In {} hour(s), it will be {}.</body></html>'.format(
        offset, dt
    )
    return HttpResponse(html)