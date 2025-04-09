# Problem Statement

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Solution

import random  

def main():
    target = random.randint(0, 99)  
    print("Guess a number between 0 and 99")

    while True:
        guess = int(input("Your guess: "))
        
        if guess < target:
            print("Too low")
        elif guess > target:
            print("Too high")
        else:
            print(f"Correct! The number was {target}")
            break

if __name__ == "__main__":
    main()

