# Problem Statement

# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Solution

def greet(name):
    print(f"Nice to have you here {name}!")
    
def main():
    user_name = input("What's your name? ")
    greet(user_name)
    
if __name__ == "__main__":
    main()
    