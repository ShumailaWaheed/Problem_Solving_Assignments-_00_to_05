# Problem Statement

# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# Solution

def main():
    curr_value = int(input("Enter a number: "))  
    
    # Continue doubling the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2  
        print(curr_value, end=" ")  
    
    print()  

if __name__ == "__main__":
    main()
