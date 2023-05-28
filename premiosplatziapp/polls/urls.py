from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    #ex /polls/
    path("", views.IndexView.as_view(), name="index"),
    #ex /polls/#/
    path("<int:pk>/detail/mejorpagina", views.DetailView.as_view(), name="detail"),  #manera que nos da django
    #ex: /polls/#/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  #para pasar pararametro variables
    #ex: 
    path("<int:question_id>/vote/", views.vote, name="vote"),  #mediante url 
]