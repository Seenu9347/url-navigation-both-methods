from app2.views import *
from django.urls import path

app_name='anime'
urlpatterns=[
    path('sasuke/',sasuke,name='sasuke'),
    path('sakura/',sakura,name='sakura'),

]
