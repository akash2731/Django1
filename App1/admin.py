from django.contrib import admin
from .models import Model1


class Ad(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'phone', 'date')


admin.site.register(Model1, Ad)
