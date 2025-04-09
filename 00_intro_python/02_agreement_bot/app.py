# Problem Statement

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!

# Solution

def main():
    # Ask the user for favorite animal
    favorite_animal = input("What's your favorite animal? ")
    
    # Respond usinf the input
    print("My favorite animal is also " + favorite_animal + "!")
   
if __name__ == '__main__':
    main()