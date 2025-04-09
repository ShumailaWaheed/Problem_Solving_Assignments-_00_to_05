# Problem Statement

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Solution

def main():
    items = [] 

    while True:
        entry = input("Enter values:")
        if entry == "":
            # Exit the loop if user enters nothing
            break  
        items.append(entry) 

    print("\nHere's the list:", items)

if __name__ == "__main__":
    main()
