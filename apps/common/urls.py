from django.urls import path
from . import views


app_name = "common"


urlpatterns = [
    path("record/add", views.add, name="add"),
]