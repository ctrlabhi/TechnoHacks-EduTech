import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),  # Ensure at least one uppercase letter
        random.choice(string.ascii_lowercase),  # Ensure at least one lowercase letter
        random.choice(string.digits),           # Ensure at least one digit
        random.choice(string.punctuation)       # Ensure at least one special character
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
