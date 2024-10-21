from django.urls import path
from .views import *
##
urlpatterns = [
    path('uploadpics/',uploadpics,name='uploadpics'),
    path('',collections,name="picstockcollections")
]
