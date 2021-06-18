from django.contrib import admin
from .models import Artical,ArticalTag

# Register your models here.

admin.site.register(ArticalTag)
admin.site.register(Artical)
# admin.site.register(Like)