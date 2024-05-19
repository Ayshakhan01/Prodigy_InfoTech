import re

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))
    consecutive_chars_criteria = not bool(re.search(r'(.)\1{2}', password))  # No consecutive characters repeated more than twice
    sequential_chars_criteria = not bool(re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)', password.lower()))  # No sequential characters like 'abc', '123', etc.

    # Calculate strength score
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria,
        consecutive_chars_criteria,
        sequential_chars_criteria
    ])

    # Provide feedback based on strength score
    if strength_score >= 7:
        return "Strong password. Excellent job!"
    elif strength_score >= 5:
        return "Moderate password strength. Consider adding more complexity."
    else:
        suggestions = [
            "Consider using a passphrase instead of a single word, like 'MyDogLikes2PlayInThePark!'",
            "Mix uppercase and lowercase letters, numbers, and special characters, like 'P@ssw0rd!2023'",
            "Combine random words with numbers and symbols, like 'PurpleBanana42$'",
            "Use a combination of initials, numbers, and symbols, like 'J0hn$mith2023!'"
        ]
        return "Weak password. Please choose a stronger password. Here are some suggestions:\n" + "\n".join(suggestions)

def main():
    # Prompt user to enter a password
    password = input("Enter your password: ")

    # Check password strength
    result = check_password_strength(password)

    # Display feedback
    print(result)

if __name__ == "__main__":
    main()
