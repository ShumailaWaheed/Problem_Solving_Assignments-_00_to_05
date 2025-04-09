# Problem Statement

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1.Prompt the user to enter the first number.
# 2.Read the input and convert it to an integer.
# 3.Prompt the user to enter the second number.
# 4.Read the input and convert it to an integer.
# 5.Calculate the sum of the two numbers.
# 6.Print the total sum with an appropriate message.

# Solution

def main():
    # Get the first number as a string input and convert to integer
    first_number_str = input("Enter the first number: ")
    first_number = int(first_number_str)
    
    # Get the second number as a string input and convert to integer
    second_number_str = input("Enter the second number: ")
    second_number = int(second_number_str)
    
    # Calculate the sum of both numbers
    total = first_number + second_number
    
    print("The sum of", first_number, "and", second_number, "is", total)

if __name__ == '__main__':
    main()