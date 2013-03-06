import prob019func

year = 1900
month = 1

dayofweek = 2 #Sunday = 1, Saturday = 7
total = 0

while year < 2001:
    
    days = prob019func.days_in_month(month, year)
    dayofweek = (dayofweek + days) % 7

    if year >= 1901 and dayofweek == 1:
        total += 1

    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(total)
