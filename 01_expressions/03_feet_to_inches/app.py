# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution

def main():
    #Ask the number of feet
    feet = float(input("Please enter the number of feet: "))
    
    # Perform the conversion
    inches = feet * 12
    
    print(f"\n🎉 {feet} foot{"s" if feet != 1 else ""} is equal to {inches} inches.🚀")
    
if __name__ == "__main__":
    main()