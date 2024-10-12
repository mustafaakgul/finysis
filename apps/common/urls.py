from django.urls import path
from . import views


app_name = "common"


urlpatterns = [
    path("", views.index, name="index"),
    path("cumulative", views.cumulative, name="cumulative"),
    path("single-data", views.single_data, name="single-data"),

    path("record/insert", views.insert_data, name="insert-data"),

    # http://localhost:8000/core/record/insert/28.02.2022
    path("record/insert/<str:date>", views.insert_by_month, name="insert-by-month"),
    path("record/cumulative", views.get, name="get"),
]