import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    required = []
    if use_upper:
        chars += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += symbols
        required.append(random.choice(symbols))
    remaining = [random.choice(chars) for _ in range(length - len(required))]
    password = required + remaining
    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 1
    if score <= 2: return "Weak 🔴"
    if score <= 3: return "Medium 🟡"
    return "Strong 🟢"

def main():
    print("=== Password Generator ===
")
    try:
        length = int(input("Password length (default 12): ").strip() or "12")
        count = int(input("How many passwords? (default 1): ").strip() or "1")
    except ValueError:
        length, count = 12, 1

    use_upper = input("Include uppercase? (y/n, default y): ").strip().lower() != "n"
    use_digits = input("Include numbers? (y/n, default y): ").strip().lower() != "n"
    use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != "n"

    print("
Generated Passwords:
")
    for i in range(count):
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        strength = check_strength(pwd)
        print(f"  {i+1}. {pwd}  ({strength})")

if __name__ == "__main__":
    main()
