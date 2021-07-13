from django.contrib.admin import site
from .models import *

site.register(IsolationRoom)
site.register(SpecialRoom)
site.register(ICUModels)
