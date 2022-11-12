from django.contrib import admin
from applications.redirect.models import Redirect
# Register your models here.

class RedirectAdmin(admin.ModelAdmin):
    list_display = (
        'key',
        'url',
        'active',
        'created_at',
        'updated_at',
    )


admin.site.register(Redirect, RedirectAdmin)



