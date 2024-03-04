from my_work.application.salary import calculate_salary
from my_work.application.db.people import get_employees
from datetime import datetime
from art import tprint

today = datetime.date(datetime.today())
f_today = today.strftime("%d.%m.%Y")

if __name__ == '__main__':
    tprint(f_today, font='block', chr_ignore=True)
    print(get_employees())
    print(calculate_salary())
