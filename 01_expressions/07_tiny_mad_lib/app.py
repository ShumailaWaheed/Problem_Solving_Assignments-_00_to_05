# Problem Statement

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Solution

def main():
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Prompting the user for inputs
    adjective = input("✨ Please type an adjective and press enter: ")
    noun = input("🌱 Now type a noun and press enter: ")
    verb = input("🚀 Finally, type a verb and press enter: ")

    # final fun sentence
    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == "__main__":
    main()
