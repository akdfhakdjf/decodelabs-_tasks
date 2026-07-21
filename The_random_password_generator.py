import secrets
import string
import math

def build_character_pool(use_symbols: bool) -> str:
    """Combine letters, digits, and (optionally) punctuation into one pool."""
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool += string.punctuation
    return pool

def generate_password(length: int, use_symbols: bool = True) -> str:
    """Generate a cryptographically secure random password of the given length."""
    pool = build_character_pool(use_symbols)
    # secrets.choice() is used instead of random.choice() because it draws
    # from the OS's cryptographically secure entropy source, not a
    # predictable pseudo-random generator like the Mersenne Twister.
    password_characters = [secrets.choice(pool) for _ in range(length)]
    # ''.join() builds the final string in one allocation (O(n)) instead of
    # repeatedly using += , which would create a new string object on every
    # iteration since Python strings are immutable (O(n^2)).
    return "".join(password_characters)

def calculate_entropy(length: int, pool_size: int) -> float:
    """E = L * log2(R) -- bits of entropy for the generated password."""
    return length * math.log2(pool_size)

def main():
    print("===== RANDOM PASSWORD GENERATOR =====")
    while True:
        raw_length = input("Enter desired password length (minimum 8): ").strip()
        try:
            length = int(raw_length)
            if length < 8:
                print("For real security, please choose at least 8 characters.")
                continue
            break
        except ValueError:
            print("That's not a valid whole number. Please try again.")

    symbols_choice = input("Include special symbols (@, #, $, etc)? (y/n): ").strip().lower()
    use_symbols = symbols_choice == "y"
    password = generate_password(length, use_symbols)
    pool_size = len(build_character_pool(use_symbols))
    entropy = calculate_entropy(length, pool_size)

    print("\n--- Your Secure Password ---")
    print(password)
    print(f"Length: {length} characters")
    print(f"Estimated entropy: {entropy:.1f} bits")


if __name__ == "__main__":
    main()
