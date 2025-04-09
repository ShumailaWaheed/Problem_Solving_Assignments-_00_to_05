# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Solution

def check_voting_eligibility(age):
    # Check if the user can vote in each country
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")
    
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")
    
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

def main():
    age = int(input("How old are you? "))
    
    # Check if they can vote in any of the countries
    check_voting_eligibility(age)

if __name__ == "__main__":
    main()
