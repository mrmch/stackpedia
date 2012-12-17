from django.contrib import admin

from models import *

admin.site.register(Contributor)
admin.site.register(Project)
admin.site.register(License)
admin.site.register(Stack)
admin.site.register(Node)

