# Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

# Solution

import random
 
def main():
    print("Rolling two dice...🎲🎲")
    
    # Role the dice
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    print(f"die 1 rolled: {die1}")
    print(f"die 2 rolled: {die2}")
    
    total = die1 + die2
    
    print(f"total of bot dice {total}")
    
if __name__ == "__main__":
    main()