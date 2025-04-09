# Problem Statement

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# Solution

import math

def main():
    print("Welcome to the Pythagorean Theorem Calculator! 📐")

    # lengths of the two perpendicular sides
    AB = float(input("Enter the length of AB (side 1): "))
    AC = float(input("Enter the length of AC (side 2): "))

    # Calculate the hypotenuse 
    BC = math.sqrt(AB ** 2 + AC ** 2)

    print(f"\n✨ According to the Pythagorean theorem:")
    print(f"✨ The length of the hypotenuse (BC) is: {BC:.2f} units.")

  
    print("\n📏 Thanks for using the Pythagorean Theorem Calculator! 🌟")

if __name__ == "__main__":
    main()
