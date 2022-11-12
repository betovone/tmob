from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from django.views.generic import View

from .models import Redirect
from .serializers import RedirectSerializer

class RedirectByKey(View):

    def get(self, request, *args, **kwargs):
        r = Redirect.objects.get_redirect(self.kwargs['key'])
        if len(r) > 0: 
            r = r[0]
            return JsonResponse(
                {
                    'key': r.key,
                    'url': r.url
                }
            )
        else:
            return JsonResponse({})

class RedirectByKeyRest(ListAPIView):
    serializer_class = RedirectSerializer

    def get_queryset(self):
        return Redirect.objects.get_redirect(self.kwargs['key'])





