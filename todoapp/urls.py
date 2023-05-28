from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.homepage, name="home"),
    path("deleteitem/<str:pk>/", views.deleteitem, name="deleteitem"),
    path("update/<str:id>/", views.updateitem, name="update")
]