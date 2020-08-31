from django.contrib import admin
from django.urls import path

from .views import HelloView
from .views import SomeTemplateView
from .views import ChairListJsonView


app_name = 'bench'

urlpatterns = [
    path('', HelloView.as_view(), name='home'),
    path('template/', SomeTemplateView.as_view(), name='template'),
    path('chairs/', ChairListJsonView.as_view(), name='query')
]
