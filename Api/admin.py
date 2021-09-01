from django.contrib import admin

from Api import models

# Register your models here.

admin.site.register(models.Leads)
admin.site.register(models.Agent)
admin.site.register(models.Products)
