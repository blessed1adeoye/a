from django.urls import path
from .views import *

app_name = 'b'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('education/', educate, name='educate'),
    path('Portfolio/', port, name='port'),
    path('Contact-me/', contact, name='contact'),
    # path('', include('b.urls', namespace='b')),
]