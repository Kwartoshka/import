from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt

print('Hi')

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    date_now = dt.datetime.today()
    date_now = dt.datetime.date(date_now)
    print(date_now)