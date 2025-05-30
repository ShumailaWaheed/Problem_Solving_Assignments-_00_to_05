# Problem Statement

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Solution

import time

def main():
    # Start the countdown from 10 and go down to 1
    for i in range(10, 0, -1):
        print(i, end=" ", flush=True) 
        time.sleep(1)  
    print("Liftoff!")  

if __name__ == "__main__":
    main()

