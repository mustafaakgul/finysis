from django.test import TestCase, SimpleTestCase

from utils.currency import CurrencyExchange


class CurrencyTests(SimpleTestCase):

    def test_usd_currency(self):
        currency_object = CurrencyExchange()
        usd_value = currency_object.get_current_rate('USD', 'BanknoteBuying')

        self.assertEqual('a', usd_value)
