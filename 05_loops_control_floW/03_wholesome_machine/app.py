# Problem Statement

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Solution

import random

def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    # List of motivational quotes 
    motivational_quotes = [
       "Believe in yourself and all that you are.",
       "Our doubts of today are the only limit to our realization of tomorrow.",        
       "You are more resilient than you realize.",        
       "Do what the clock says, not the other way around. Keep going.",
       "Act as if your actions have an impact. It does.",
       "The best way to predict the future is to create it."
    ]
    
    print(f"Please type the following affirmation: {affirmation}")
    
    while True:
        user_input = input().strip()  
        if user_input.lower() == affirmation.lower():  
            print("That's right! :) You're amazing!")
            break
        else:
            # Randomly pick a motivational quote when the user gets it wrong
            print(f"Hmmm, that was not the affirmation.")
            print(f"Here's a motivational quote to keep you going: {random.choice(motivational_quotes)}")
            print(f"Please type the following affirmation: {affirmation}")

if __name__ == "__main__":
    main()