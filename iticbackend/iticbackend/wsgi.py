"""
WSGI config for iticbackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#sys.path.append('/home/revan/Desarrollo/Back-end-ITIC/iticbackend')
#os.environ['DJANGO_SETTING_MODULE']="iticbackend.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iticbackend.settings')

application = get_wsgi_application()
