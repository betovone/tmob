from django.urls import path

from . import views

app_name = 'redirect_app'

urlpatterns = [
    path(
        'api/redirect/by-key/<key>/',
        views.RedirectByKey.as_view(),
        name='redirect-by-key',
    ),
    path(
        'api/redirect/by-key-rest/<key>/',
        views.RedirectByKeyRest.as_view(),
        name='redirect-by-key-rest',
    ),
]
