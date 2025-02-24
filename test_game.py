from day_of_week_game import *
import json
import pytest

@pytest.fixture(scope="module")  # Load JSON data once per module (test file)
def date_day_data():
    with open("date_day.json", 'r') as f:
        return json.load(f)

day_name_to_number = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}

def test_calculate_day_of_week_against_json(date_day_data):
    """
    Pytest function to test calculate_day_of_week against dates in date_day_output.json.
    """
    mismatches = []
    for date_str, expected_day_name in date_day_data.items():
        year, month, day = map(int, date_str.split('-'))
        calculated_day_number = calculate_day_of_week(year, month, day)
        expected_day_number = day_name_to_number[expected_day_name]

        assert isinstance(calculated_day_number, int), f"For date {date_str}, calculate_day_of_week did not return an integer. Got: {calculated_day_number}"
        assert 0 <= calculated_day_number <= 6, f"For date {date_str}, calculate_day_of_week returned an invalid day number: {calculated_day_number}. Expected 0-6."
        assert calculated_day_number == expected_day_number, f"Mismatch for date {date_str}. Expected {expected_day_name} (number {expected_day_number}), but got day number {calculated_day_number}."

        if calculated_day_number != expected_day_number:
            mismatches.append({
                "date": date_str,
                "expected_day": expected_day_name,
                "calculated_day_number": calculated_day_number
            })

    if mismatches:
        error_message = "Day of week mismatches found:\n"
        for mismatch in mismatches:
            error_message += (
                f"  Date: {mismatch['date']}, Expected: {mismatch['expected_day']}, "
                f"Calculated Number: {mismatch['calculated_day_number']}\n"
            )
        pytest.fail(error_message) # Fail the pytest test if mismatches exist
    else:
        print("\nAll day of week tests passed against date_day_output.json!") # Optional success message when run directly (not pytest)


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
    

def test_user_input(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_user_guess() == 1


