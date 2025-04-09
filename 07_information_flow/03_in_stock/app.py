# Problem Statement

# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:
# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock
# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)
# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.
# Here's two sample runs of the program (user input in bold italics):
# Enter a fruit: pear
# This fruit is in stock! Here is how many:
# 1000
# Enter a fruit: lychee
# This fruit is not in stock.

# Solution

# inventory dictionary for Sophia's fruit store
inventory = {
    "apple": 50,
    "banana": 25,
    "pear": 1000,
    "orange": 0,
    "grape": 15
}

def num_in_stock(fruit):
    # Returns the number of that fruit in inventory or 0 if not found
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()  
    stock = num_in_stock(fruit) 

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
