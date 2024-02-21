import pandas as pd
import xlrd
import os

from django.test import TestCase, SimpleTestCase


class HelloTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_hello(self):
        response = "hello"
        data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name='31.01.2022')

        # for i in range(0, 5):
        #     for j in range(0, 3):
        #         # Print the cell values with tab space
        #         print(data.cell_value(i, j), end='\t')
        #     print('')

        data.to_sql('mizan', 'sqlite:///db.sqlite3', if_exists='replace', index=False)

        size = data.size
        info = data.info()
        few_rows = data.head()

        self.assertEqual(response, "hello")
