# Problem Statement

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

# Solution

def double_elemets(numbers):
    
    return [num * 2 for num in numbers]

def main():
    print("🔁 Let's play double the numbers in your list!")
    
    # Original list of numbers
    numbers =[1,2,3,4,5]
    print(f"Original list: (numbers)")
    
    # Doubled list
    doubled = double_elemets(numbers)
    print(f"Doubled list: {doubled} 🎯")
    
if __name__ == "__main__":
    main()
