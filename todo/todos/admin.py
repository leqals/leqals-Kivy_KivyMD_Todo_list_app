from django.contrib import admin
from .models import *

mods = [Userprofile, Todo]
for model in mods : admin.site.register(model)