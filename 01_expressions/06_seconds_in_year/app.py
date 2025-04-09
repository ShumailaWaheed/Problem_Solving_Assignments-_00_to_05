# Problem Statement

# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# Solution

def main():
    DAYS_IN_YEAR = 365
    HOURSE_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    #Calcukate total seconds in a year
    seconds_in_year =DAYS_IN_YEAR * HOURSE_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    
    print(f"⏰ Did you know? ✨ There are {seconds_in_year} Seconds in a year! 🎉")

if __name__ == "__main__":
    main()