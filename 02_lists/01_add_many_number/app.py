# Problem Statement

# Write a function that takes a list of numbers and returns the sum of those numbers.

# Solutions

def sum_numbers(numbers):
    
    return sum(numbers)

def main():
    print("🔢 Let's add some numbers togather!")
    
    # Taking numbers as input
    input_str = input("Please enter numbers separated by commas (e.g., 1,2,3): ")
    
    #list of floats
    number_list = [float(num.strip()) for num in input_str.split(",")]
    
    total = sum_numbers(number_list)
    
    print(f"The total sum of your numbers is: {total} ✅")
    
if __name__ == "__main__":
    main()
