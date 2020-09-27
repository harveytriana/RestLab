#API View (another approach) 
from django.urls import path
from quickstart import views

urlpatterns=[
    # http://127.0.0.1:5004/api/hello -> load views.HelloApiView
    #
    path('hello', views.HelloApiView.as_view()),
]