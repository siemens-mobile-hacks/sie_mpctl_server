import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sie_mpctl.settings')
application: any = get_wsgi_application()
