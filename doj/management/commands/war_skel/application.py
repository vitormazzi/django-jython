from django.core.handlers import wsgi
import os

def handler(environ, start_response):
    os.putenv("DJANGO_SETTINGS_MODULE", "{{ settings.SETTINGS_MODULE }}")
    workaround_modjy_passing_unicode_values(environ)
    h = wsgi.WSGIHandler()
    return h(environ, start_response)

# Workaround for jython bug #1245
def workaround_modjy_passing_unicode_values(environ):
    for key in environ:
        if key.startswith('HTTP_') and \
               isinstance(environ[key], unicode):
            environ[key] = environ[key].encode('iso-8859-1')
