# Problem Statement

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# Solution

def main():
    number_counts = {}

    while True:
        number = input("Enter a number: ")

        # If input is empty, stop collecting numbers
        if not number:
            break

        number = int(number)

        # Update the count for the entered number in the dictionary
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    for num, count in number_counts.items():
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    main()
