from django.urls import path

from apps.views import healthchk

urlpatterns = [
    path('healthchk', healthchk)
]