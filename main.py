from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print('now ', datetime.today().strftime('%d/%m/%Y %H:%M'))
    get_employees()
    calculate_salary()




