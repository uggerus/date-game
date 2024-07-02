from day_of_week_game import *

def test_calculate_day_of_week():
    assert calculate_day_of_week(2000, 9, 12) == 2
    assert calculate_day_of_week(1900, 2, 28) == 3
    assert calculate_day_of_week(1891, 1, 1) == 4
    assert calculate_day_of_week(1582, 10, 15) == 5
    assert calculate_day_of_week(1624, 12, 15) == 0
    assert calculate_day_of_week(1776, 7, 4) == 4
    assert calculate_day_of_week(1984, 8, 11) == 6
    assert calculate_day_of_week(2555, 3, 2) == 0
    assert calculate_day_of_week(1646, 4, 2) == 1
    assert calculate_day_of_week(2199, 5, 11) == 6
    
    
def test_day_name_from_number():
    assert day_name_from_number(0) == "Sunday"
    assert day_name_from_number(1) == "Monday"
    assert day_name_from_number(2) == "Tuesday"
    assert day_name_from_number(3) == "Wednesday"
    assert day_name_from_number(4) == "Thursday"
    assert day_name_from_number(5) == "Friday"
    assert day_name_from_number(6) == "Saturday"



def test_month_name_from_number():
    assert month_name_from_number(1) == "January"
    assert month_name_from_number(2) == "February"
    assert month_name_from_number(3) == "March"
    assert month_name_from_number(4) == "April"
    assert month_name_from_number(5) == "May"
    assert month_name_from_number(6) == "June"
    assert month_name_from_number(7) == "July"
    assert month_name_from_number(8) == "August"
    assert month_name_from_number(9) == "September"
    assert month_name_from_number(10) == "October"
    assert month_name_from_number(11) == "November"
    assert month_name_from_number(12) == "December"
    
