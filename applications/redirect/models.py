from django.db import models
from django.db.models.signals import post_save

from .signals import cache_redirect
from .managers import RedirectManager

class BaseTimeStamp(models.Model):
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Modificado", auto_now=True)
  
    class Meta:
        abstract = True


class Redirect(BaseTimeStamp):
    LONG_KEY = 50
    LONG_URL = 200

    key = models.CharField("Key", max_length=LONG_KEY, unique=True, db_index=True)
    url = models.URLField("Url", max_length=LONG_URL)
    active = models.BooleanField("Activo", default=True)
    
    class Meta:
        verbose_name = 'Redirección'
        verbose_name_plural = 'Redirecciones'
        ordering = ['-created_at']

    objects = RedirectManager()

    def __str__(self):
        return "{} - {}".format(self.key, self.url)


# signals 
post_save.connect(cache_redirect, sender=Redirect)
