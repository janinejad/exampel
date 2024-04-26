from django.urls import path
from .views import hello,contact,about
app_name = 'blog'
urlpatterns = [
    path('contact-us/',contact,name='contact'),
    path('about/',about,name='about')
]
