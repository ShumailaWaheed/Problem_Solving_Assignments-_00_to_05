# Problem Statement

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# Solution

def main():
    # Minimum height required to ride
    MIN_HEIGHT = 50
    
    while True:
        height = input("How tall are you? ")

        # If the user doesn't enter anything, break the loop
        if not height:
            print("Thanks for using the ride checker!")
            break
        try:
            height = int(height)

            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        
        except ValueError:
            # Handle case where the user input is not a number
            print("Oops! That doesn't seem like a valid height. Please enter a number.")

if __name__ == "__main__":
    main()


