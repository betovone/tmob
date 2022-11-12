from django.db import models
from django.core.cache import cache


class RedirectManager(models.Manager):
    def get_redirect(self, key):
        datos = cache.get('redirects')
        resultado = []
        if datos:
            resultado = cache.get('redirects').filter(key=key)

        return resultado

