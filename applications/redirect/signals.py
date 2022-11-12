from django.core.cache import cache

def cache_redirect(sender, instance, **kwargs):
    cache.set('redirects', sender.objects.filter(active=True))
    return instance  

