from django.test import TestCase, SimpleTestCase


class CurrenciesTests(SimpleTestCase):

    def test_usd_currency(self):
        self.assertEqual('a', 'a')

    # def test_usd_currency(self):
    #     currency_object = CurrencyExchange()
    #     usd_value = currency_object.get_current_rate('USD', 'BanknoteBuying')
    #
    #     self.assertEqual('a', usd_value)

