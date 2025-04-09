# Problem Statement

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

# Solution

def in_range(n, low, high):
    # Check if the number is between low and high
    return low <= n <= high

def main():
    # ask the user for three values: number, lower bound, and upper bound
    number = int(input("Enter a number: "))
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    
    result = in_range(number, lower, upper)
    print(result)
    
if __name__ == "__main__":
    main()