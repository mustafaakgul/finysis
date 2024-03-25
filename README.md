## Track and visualize financial data with a Django analytics project

### Financial Notes in Tr
* Borç bakiyesi ve alacak bakiyesi kümülatif degil ve direk gözüküyor
* Borç ve alacak gözükmüyor
* 999 a kadar standart, sonrası sirkete gore değişiyor


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