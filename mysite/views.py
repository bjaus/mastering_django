from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {}.</body></html>".format(now)
    return HttpResponse(html)
    
    
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