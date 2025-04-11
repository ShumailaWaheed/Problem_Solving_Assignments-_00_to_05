# Problem Statement

# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

# Solution

def get_name():
    # Assignig name to a variable
    my_name = "Shumaila"
    return my_name

def main():
    name = get_name()
    
    # Retrieed name to print a customized greetings
    print("Howday " + name + "! 🤠")
    
if __name__ == "__main__":
    main()
