def days_in_month(month, year):
    days = {1: 31, 3: 31, 4: 30, 5: 31,
            6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    else: 
        return days[month]


def is_leap_year(year):

    if year % 100 == 0: #Century
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False
