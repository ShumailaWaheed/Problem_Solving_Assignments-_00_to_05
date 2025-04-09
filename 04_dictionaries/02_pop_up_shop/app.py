# Problem Statement

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Solution

def main():
    #  price list for each fruit 
    fruit_prices = {
        "apple": 2.5,
        "durian": 5.0,
        "jackfruit": 3.0,
        "kiwi": 4.0,
        "rambutan": 6.5,
        "mango": 2.0
    }

    total = 0 

    # Iterate through each fruit and its price
    for fruit, price in fruit_prices.items():
        try:
            quantity = int(input(f"How many {fruit}s would you like to buy? "))
            total += price * quantity
        except ValueError:
            print("Please enter a valid number.")

    print(f"Your total cost for the fruits is ${total:.2f}")

if __name__ == "__main__":
    main()
