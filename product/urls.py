from django.urls import path
from .views import htmlview


urlpatterns = [
    path('html/',htmlview)
]
