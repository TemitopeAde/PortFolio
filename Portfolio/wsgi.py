import os
import sys
​
path = '/home/temade123/temade123.pythonanywhere.com')
if path not in sys.path:
    sys.path.append(path)
​
os.environ['DJANGO_SETTINGS_MODULE'] = 'Portfolio.settings'
​
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()