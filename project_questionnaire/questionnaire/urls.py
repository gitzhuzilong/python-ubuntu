from django.conf.urls import url
from questionnaire import views

urlpatterns = [
    url(r'^index$', views.index),
]