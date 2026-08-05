import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root directory to the python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apptim.settings")

application = get_wsgi_application()
app = application
