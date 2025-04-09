# Problem Statement

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Solution

def main():
    # input length of the triangle sides
    length_a: float = float(input("What is the length of side 1? "))
    length_b: float = float(input("What is the length of side 2? "))
    length_c: float = float(input("What is the length of side 3? "))

    # Calculate perimeter
    print("The perimeter of the triangle is " + str(length_a + length_b + length_c))

if __name__ == '__main__':
    main()