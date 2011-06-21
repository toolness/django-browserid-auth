from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

# TODO: This should be a setting.
BROWSERID_INCLUDE_SCRIPT = 'https://browserid.org/include.js'

def login_form(request):
    c = RequestContext(request)
    return render_to_response(
        'browserid_login.html',
        {
            'browserid_include_script': BROWSERID_INCLUDE_SCRIPT
        },
        context_instance=c
        )

def verify_login(request):
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'],
                            assertion=request.POST['assertion'])
        if user is not None:
            if user.is_active:
                login(request, user)
                # TODO: '/' should really be a setting.
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('your account is disabled.')
        else:
            return HttpResponse('access denied')
    else:
        return HttpResponseNotAllowed(['POST'])
