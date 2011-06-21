from django.http import HttpResponse

def home(request):
    return HttpResponse('O HAI %s' % (request.user))
