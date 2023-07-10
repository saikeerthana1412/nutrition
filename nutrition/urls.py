from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns= [
    path('', views.say_hello)
    path('submitrequest/', views.submit_request),
]

#urlpatterns+=staticfiles_urlpatterns()

