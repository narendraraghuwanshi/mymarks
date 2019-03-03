from django.conf import settings
from django.db import models
from django.contrib import messages
from django.db import connections
from django.db.utils import OperationalError
from django.http import HttpResponseRedirect

class SubdoainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        settings.ALLOWED_HOSTS = ["*"]
        # One-time configuration and initialization.


    def __call__(self, request):
        domain_parts = request.get_host().split('.')
        if (len(domain_parts) > 2):
            subdomain = domain_parts[0]
            if (subdomain.lower() == 'www'):
                subdomain = None
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = None
            domain = request.get_host()


        request.subdomain = subdomain
        request.domain = domain




        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


    def __call__(self, request):
        settings.SITE_ID =2
        domain_parts = request.get_host().split('.')
        if (len(domain_parts) > 2):
            subdomain = domain_parts[0]
            settings.DATABASES['default']['NAME'] = 'mymarks_' + subdomain
            db_conn = connections['default']
            try:
                c = db_conn.cursor()
            except OperationalError:
                # messages.error(request, 'Database Not Found ! Please Contact Administrator')
                subdomain = None
                settings.DATABASES['default']['NAME'] = 'mymarks'
                return HttpResponseRedirect("http://snrorg.com")
            if (subdomain.lower() == 'www'):
                subdomain = None
                settings.DATABASES['default']['NAME'] = 'mymarks'
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = None
            domain = request.get_host()


        request.subdomain = subdomain
        request.domain = domain

        # print( subdomain)

        # settings.DATABASES = {
        #     'default': {
        #         'ENGINE': 'djongo',
        #         'NAME': 'mymarknew',
        #     }
        # }


        print(settings.DATABASES['default']['NAME'])


        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response