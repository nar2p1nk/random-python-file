from datetime import datetime, timedelta

def calculateDate(t):

    dateNow = datetime.now()

    print(f'date today: {dateNow}')

    date2days = dateNow + timedelta(days=t)

    print(f'date after {t} day: {date2days}')


calculateDate(5)