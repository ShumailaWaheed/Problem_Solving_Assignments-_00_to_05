#vProblem Statement

# Print 10 random numbers in the range 1 to 100.

# Solution

import random
    
def main():
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
        
if __name__ == "__main__":
    main()
    
