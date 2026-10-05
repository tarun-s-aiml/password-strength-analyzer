import re


def analyze_password(password):

    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, feedback


print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter password: ")

score, strength, feedback = analyze_password(password)

print("\n===== ANALYSIS =====")
print("Score    :", f"{score}/5")
print("Strength :", strength)

if feedback:
    print("\nSuggestions:")

    for item in feedback:
        print("-", item)
else:
    print("\nExcellent! Your password meets all basic requirements.")
