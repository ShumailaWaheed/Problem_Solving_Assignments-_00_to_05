# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# Solution

MAX_LENGTH: int = 3

def shorten(items):
    while len(items) > MAX_LENGTH:
        print(items.pop())

def collect_items():
    result = []
    while True:
        entry = input("Enter a list item leave blank to finish: ")
        if not entry:
            break
        result.append(entry)
    return result

def main():
    user_list = collect_items()
    shorten(user_list)

if __name__ == "__main__":
    main()
