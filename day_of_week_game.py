
def  calculate_day_of_week(year, month, day):
    t = 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4
    if month < 3:
        year-=1
    return (year + year//4 - year//100 + year//400 + t[month - 1] + day) % 7
