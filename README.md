## Track and visualize financial data with a Django analytics project
* Those ending with 'e' or 'd' are excluded from USD conversion.
* Use end-of-month rates for those below 600, and average rates for the others.
* For quarterly or annual average reports, those values will be used; otherwise, monthly values will be used for calculations.
* Accounts 1-5 (balance sheet) use end-of-period exchange rates (as they show debit and credit), while accounts 6-7 (profit and loss) use average exchange rates.

### Financial Notes
* 999 stardart, others can be changed by companies
* Four decimal places for currencies


### To Test (Python Console)
* usd = cur.get_current_rate('USD', 'BanknoteBuying')


### How to Run
* python3.12 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver


### Structure
* Business Logic: https://sunscrapers.com/blog/where-to-put-business-logic-django/


### To Do