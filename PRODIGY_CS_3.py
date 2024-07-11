import re

def password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_message = strength_levels[strength - 1] if strength > 0 else "Very Weak"

    return strength_message, feedback

def main():
    password = input("Enter your password: ")
    strength_message, feedback = password_strength(password)
    print(f"Password Strength: {strength_message}")

    if feedback:
        print("Feedback to improve your password:")
        for tip in feedback:
            print(f" - {tip}")

if __name__ == "__main__":
    main()
