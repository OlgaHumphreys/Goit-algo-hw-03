import datetime

def get_days_from_today(date: str) -> int|str:
    """Function calculate amount of days between target date and current date"""
    try:
        date_object = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.datetime.today().date()
        delta_dates = current_date - date_object
        return delta_dates.days
    except ValueError:
        return "Wrong format, should be YYYY-MM-DD"

print(get_days_from_today("2024 10 09"))




