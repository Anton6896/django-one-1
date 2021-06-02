import sys
from .base import *

"""
dont forget to add BASE_DIR parent dir !! because of different settings 
"""

if "/home/ant/Documents/django-one-1/root/settings/__init__.py" == __file__:
    from .local import *

    print(" ---- you at local env settings ---- ")
else:
    from .prod import *
