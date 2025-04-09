# Problem Statement

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

# Solution

import random

def roll_dice():
    
    #Roll two dice and return their values
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1, die2

def main():
    print("🎲 Welcome to the Dice Rolling! 🎲\n")
    
    # Rolling dice three times
    for i in range(1,4):
        print(f"Roll {i}:")
        die1, die2 = roll_dice()
        print(f" - Dice 1: {die1}")
        print(f" - Dice 2: {die2}\n")
        
if __name__ == "__main__":
    main()