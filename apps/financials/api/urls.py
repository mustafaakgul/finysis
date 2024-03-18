from django.urls import path
from apps.financials.api.views import GetFinancials


app_name = "financials"


urlpatterns = [
    path("get", GetFinancials.as_view(), name="get_financials"),
]