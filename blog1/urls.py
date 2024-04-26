from django.urls import path
from .views import contact, about,get_plan

app_name = 'blog'
urlpatterns = [
    path('contact-us/', contact, name='contact'),
    path('about/', about, name='about'),
    path('body-building-plan/<int:day_id>', get_plan, name='body_building_plan')
]
