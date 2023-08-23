from django.urls import path
from . import views

app_name = "dogs"
urlpatterns = [
    path("", views.Index, name="index"),
    path("dogs/adoptable/", views.AdoptableView.as_view(), name="adoptable"),
    path("dogs/<int:pk>/", views.DetailView.as_view(), name="detail")
]
