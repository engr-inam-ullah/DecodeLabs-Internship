import string
import secrets

# character pools
letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*"

def get_length():
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Password should be at least 8 characters long.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")


def generate_password(length, use_symbols=True):
    pool = letters + digits
    if use_symbols:
        pool += symbols

    # make sure password isn't super weak - at least one letter, one digit
    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits)
    ]

    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    remaining = length - len(password_chars)
    password_chars += [secrets.choice(pool) for _ in range(remaining)]

    # shuffle so the guaranteed chars aren't always at the start
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("---- Random Password Generator ----")
    length = get_length()

    choice = input("Include special characters (@, #, $ etc)? (y/n): ").strip().lower()
    use_symbols = choice == "y"

    password = generate_password(length, use_symbols)
    print(f"\nYour generated password:\n{password}")


if __name__ == "__main__":
    main()