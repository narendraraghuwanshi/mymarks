from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
     return render(request, 'login/index.html')


def check(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username', '').strip(),
            password=request.POST.get('password', ''),
        )
        if user is None:
            messages.warning(request, u'Invalid credentials')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
            else:
                messages.error(request, u'User is not active.')
                return render(request, 'login/index.html')
def logoutuser(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(request.GET.get('next', '/login'))