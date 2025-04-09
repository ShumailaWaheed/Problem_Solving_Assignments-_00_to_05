# Problem Statement

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

# Solution

def subtract_seven(num):
    
    return num - 7

def main():
    # Ask the user to enter a number
    number = int(input("Enter a number: "))
    
    result = subtract_seven(number)
    
    print("After subtracting 7, the result is:", result)
    
if __name__ == "__main__":
    main()