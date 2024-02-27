from django.urls import path
from . import views


app_name = "currencies-web"


urlpatterns = [
    path("add", views.add_this_month, name="add_this_month"),
]