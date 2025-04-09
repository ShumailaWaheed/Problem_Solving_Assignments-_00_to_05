# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# Solution

def get_first_element(lst):
    print(f"\n✅ First element in the list: {lst[0]}")
    
def main():
    total = int(input("🔢 How many elements would you like to add? "))
    
    user_list = []
    # Loop to collect elements
    for i in range(1, total + 1):
        item = input(f"📝 Enter item #{i}: ")
        user_list.append(item)
        
    get_first_element(user_list)
    
if __name__ == "__main__":
    main()
    