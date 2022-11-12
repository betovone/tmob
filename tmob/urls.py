from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #includes
    re_path('', include('applications.redirect.urls')),
]
