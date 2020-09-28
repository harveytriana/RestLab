#API View (another approach) 
from django.urls import path
from Books import views

urlpatterns=[
    # http://127.0.0.1:5004/api/booktitles 
    #
    path('booktitles', views.BookTitles.as_view()),
]
