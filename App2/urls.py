from django.urls import path
from App2.views import *

app_name='bhai'

urlpatterns=[
    path('Lipu/',Lipu,name='Lipu'),
]