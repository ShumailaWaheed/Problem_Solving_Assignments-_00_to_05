# Problem Statement

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

# Solution

def count_even(lst):
    # Collect numbers from the user until they press enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "": 
            break
        try:
            lst.append(int(user_input)) 
        except ValueError:
            print("Invalid input, please enter an integer.")

    # Count and print the even numbers 
    even_count = sum(1 for number in lst if number % 2 == 0)
    print(f"Number of even numbers: {even_count}")

def main():
    numbers = [] 
    count_even(numbers)  

if __name__ == "__main__":
    main()  
