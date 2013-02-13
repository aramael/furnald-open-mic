__author__ = 'aramael'

# Import All Common Settings Constants
from settings.common import *

# Import Location Specific Information
try:
    # Import Development Constants
    from settings.development import *
except ImportError:
    # Import Production Constants
    from settings.production import *
    pass