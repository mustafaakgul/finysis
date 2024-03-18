from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.currencies.models import Currency
from apps.financials.models import FinancialTable, Mizan


class GetFinancials(APIView):
    """
     This class-based view handles the addition of a new currency.

     It uses token-based authentication and restricts access to admin users only.

     Methods:
         post: Handles the POST request to add a new currency.
     """

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        financial = FinancialTable.objects.get(account_code="101")
        converter_type = financial.converter_type
        mizan_instance = Mizan.objects.filter(account_code="101").first()
        mizan_instance_date = mizan_instance.date
        currency = Currency.objects.get(date=mizan_instance_date)

        debit_usd = mizan_instance.debit / currency.buying
        credit_usd = mizan_instance.credit / currency.buying

        result = FinancialTable.objects.get(account_code=mizan_instance.account_code).converter_type

        return Response({"status": "success", "data": "data"})