# Problem Statement

# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

# In the Gregorian calendar, three criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.

#Solution

def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))

        # Check if the year is a leap year and output the result
        result = check_leap_year(year)
        print(result)

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Oops! That doesn't seem like a valid year. Please enter a number.")

def check_leap_year(year):
    """
    Checks if the provided year is a leap year or not.
    A year is a leap year if:
    - It's divisible by 4 but not by 100,
    - or divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Yes, that's a leap year!"
    else:
        return "No, that's not a leap year."

if __name__ == "__main__":
    main()
