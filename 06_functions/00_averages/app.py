# Problem Statement

# Write a function that takes two numbers and finds the average between the two.

# Solution

def main():
    num1 = float(input("Enter the first number: "))
    
    num2 = float(input("Enter the second number "))
    
    # Calculate the average of the two numbers
    average = (num1 + num2) / 2
    
    print(f"The average of {num1} and {num2} is: {average}")

if __name__ == "__main__":
    main()

