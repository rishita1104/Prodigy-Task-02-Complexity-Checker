import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # Strength assessment
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def main():
    print("Password Strength Checker ")
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for s in suggestions:
            print(f"- {s}")

if __name__ == "__main__":
    main()
