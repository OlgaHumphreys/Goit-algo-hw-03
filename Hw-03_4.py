import datetime


def get_upcoming_birthdays (users):
    today = datetime.datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_this_year.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        timedelta_birthday = (birthday_this_year - today).days

        if 0 <= timedelta_birthday <= 7:

            if birthday_this_year.weekday() >= 5:
                extra_days = 7 - birthday_this_year.weekday()

                next_week_day = birthday_this_year + datetime.timedelta(days=extra_days)
                upcoming_birthdays.append({'name': user["name"], 'congratulation_date': next_week_day.strftime("%Y.%m.%d")})

            else: 
                upcoming_birthdays.append({"name": user["name"],
                                           'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")})
    return upcoming_birthdays



users = [
    {"name": "John Doe", "birthday": "1985.05.01"},
    {"name": "Jane Smith", "birthday": "1990.05.05"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)










