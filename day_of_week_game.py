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

def day_name_from_number(day_of_week):
    #day_of_week must be 0-6
    assert day_of_week >= 0 and day_of_week <= 6
    t = "Sunday", "Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    return t[day_of_week]

def month_name_from_number(month):
    #month must be between 1 and 12
    assert month >= 1 and month <= 12
    t = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    return t[month-1]

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter 0 for Sunday, 1 for Monday, ..., 6 for Saturday\n"))
        except ValueError:
            print("Input must be a number")
            continue

        if guess < 0 or guess > 6:
            print("Your guess must be between 0 and 6.")
            continue
        else:
            break

    return guess

def play_game():
    #random year between 1583 and 3000
    random_year = random.randint(1583, 3000)

    random_month = random.randint(1, 12)

    #random day
    random_day = make_random_day(random_month, random_year)

    actual_day_of_week = calculate_day_of_week(random_year, random_month, random_day)
    random_date = month_name_from_number(random_month)+ " " + str(random_day) + ", " + str(random_year)
    print("Guess the day of the week for: " + random_date)

    guess = get_user_guess()


if __name__ == "__main__":
    play_game()
