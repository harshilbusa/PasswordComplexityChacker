import re

def check_password_strength(password):
    # Initialize strength and feedback
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if strength == 5:
        return "Strong Password", feedback
    elif strength >= 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback


# Input from user
password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)

# Output the result
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions for improvement:")
    for suggestion in feedback:
        print(f"- {suggestion}")





















































