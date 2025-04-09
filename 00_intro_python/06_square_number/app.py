# Problem Statement

# Ask the user for a number and print its square (the product of the number times itself).

# Solution

def main():
     # ask the user for a number
     number = float(input("👉 Please enter any number to calculate its square: "))
     
     # Calculate the square
     square = number * number
     
     print(f"✅ the square of {number} is {square}  📐 ")
     
if __name__ == "__main__":
    main()