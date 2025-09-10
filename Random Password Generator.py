import string
import secrets  # better than random for passwords

def password_generator():
    try:
        length = int(input("Enter your password length: "))
        if length <= 0:
            print(" Password length must be greater than 0.")
            return
    except ValueError:
        print(" Invalid input! Please enter a number for length.")
        return

    # Ask for character set preferences
    lowercase = input("Include lowercase letters (y/n)? : ").strip().lower().startswith("y")
    uppercase = input("Include uppercase letters (y/n)? : ").strip().lower().startswith("y")
    digits = input("Include digits (y/n)? : ").strip().lower().startswith("y")
    special_character = input("Include special characters (y/n)? : ").strip().lower().startswith("y")

    # Build character pool
    char_pool = ""
    if lowercase:
        char_pool += string.ascii_lowercase
    if uppercase:
        char_pool += string.ascii_uppercase
    if digits:
        char_pool += string.digits
    if special_character:
        char_pool += string.punctuation

    if not char_pool:
        print(" You must select at least one character type!")
        return

    # Generate the password using secrets for stronger randomness
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    print("\n Generated password:", password)


if __name__ == "__main__":
    password_generator()
