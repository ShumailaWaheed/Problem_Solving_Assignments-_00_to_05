# Problem Statement

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Solution

def main():
    print("Lat's do some division and find out the  feminder too!")
    
# Get input from the user
num1 = int(input("Enter the number you want to devide: "))  
num2 = int(input("Now enterthe number you want to devide by: "))

# Perform devision and find reminder
result = num1 // num2
leftover = num1 % num2

print(f"When you devide {num1} bt {num2}, you get {result} with {leftover} left over.")

if __name__ == "__main__":
    main()