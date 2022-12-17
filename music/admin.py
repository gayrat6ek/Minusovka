from django.contrib import admin
from .models import Minus,Music,Category,CategoryName
# Register your models here.
admin.site.register((Minus,Music,Category,CategoryName))