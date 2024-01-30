import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    # Check user preferences and add corresponding character sets
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Validate that at least one character type is selected
    if not characters:
        print("Error: Please select at least one character type.")
        return None

    # Generate the password using random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("-------------------")

    try:
        # Get user input for password length
        length = int(input("Enter the password length: "))
    except ValueError:
        # Handle the case where the user enters a non-numeric value
        print("Error: Please enter a valid numeric value for password length.")
        return

    # Get user preferences for character types
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("\nGenerated Password:")
        print(password)

if __name__ == "__main__":
    # Execute the main function if the script is run as the main program
    main()
