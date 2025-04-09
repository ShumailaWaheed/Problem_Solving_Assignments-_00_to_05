# Problem Statement

#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Solution

def get_last_element(lst):
    print(f"\n✅ Last element in the list: {lst[-1]}")
    
def main():
    count = int(input("🔢 How many elements will you enter? "))
    
    user_list = []
    # collect elements 
    for i in range(1, count + 1):
        item = input(f"📝 Enter item #{i}: ")
        user_list.append(item)
        
    get_last_element(user_list)
    
if __name__ == "__main__":
    main()
    