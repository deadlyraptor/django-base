import os
from projectname.settings.base import *

ALLOWED_HOSTS = [os.getenv('DOMAIN_NAME')]

try:
    from .local import *
except ImportError:
    pass
