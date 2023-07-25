from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns= [
    path('', views.welcome),
    path('getdata/',views.say_hello),
    path('submitrequest/',views.submit_request),
    path('submitrequest/_facts/',views.facts)
   
]

#urlpatterns+=staticfiles_urlpatterns()

