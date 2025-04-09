# Problem Statement

# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Solution

def main():
    phonebook = {}

    while True:
        name = input("Enter a name (or press Enter to stop): ")
        # Stop if the name is empty
        if not name:  
            break

        number = input(f"Enter the phone number for {name}: ")
        phonebook[name] = number  

    # Print the phonebook
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")  

if __name__ == "__main__":
    main()
