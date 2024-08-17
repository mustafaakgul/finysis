## Track and visualize financial data with a Django analytics project

### Financial Notes
* 999 stardart, others can be changed by companies
* Four decimal places for currencies


### To Test (Python Console)
* usd = cur.get_current_rate('USD', 'BanknoteBuying') //"BanknoteBuying":Alış Değeri, "BanknoteSelling":Satış Değeri


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
* Formatting currency, localization
* Validation of inserting by month
* Try to move new table cumulative mizans from old