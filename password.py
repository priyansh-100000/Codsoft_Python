import random
import string
def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 to ensure complexity.")
        return None
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

   password = [random.choice(lowercase),random.choice(uppercase), random.choice(digits), random.choice(symbols)]

    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
      return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
