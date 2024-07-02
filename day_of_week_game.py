import random

def  calculate_day_of_week(year, month, day):
    t = 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4
    if month < 3:
        year-=1
    return (year + year//4 - year//100 + year//400 + t[month - 1] + day) % 7

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def make_random_day(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month  == 10 or month == 12:
        return random.randint(1, 31)
    elif month == 4 or  month == 6 or month == 9 or month == 11:
        return random.randint(1, 30)
    else:
        if is_leap_year(year):
            return random.randint(1, 29)
        else:
            return random.randint(1, 28)
    


#random year between 1583 and 3000
random_year = random.randint(1583, 3000)

random_month = random.randint(1, 12)

#random day
random_day = make_random_day(random_month, random_year)

    
