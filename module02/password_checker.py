import re


def check_strength(password):
    length = len(password)

    categories = 0

    if re.search(r'[a-z]', password):
        categories += 1

    if re.search(r'[A-Z]', password):
        categories += 1

    if re.search(r'\d', password):
        categories += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        categories += 1

    if length >= 12:
        length_score = 2
    elif length >= 8:
        length_score = 1
    else:
        length_score = 0

    score = categories + length_score

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, score


def suggestions(password):
    tips = []

    if len(password) < 8:
        tips.append("Use at least 8 characters.")

    if not re.search(r'[A-Z]', password):
        tips.append("Add uppercase letters.")

    if not re.search(r'\d', password):
        tips.append("Include numbers.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        tips.append("Include special characters.")

    return tips


def main():
    print("Password Strength Checker")

    pwd = input("Enter password: ")

    strength, score = check_strength(pwd)

    print("Result:", strength)
    print("Score:", str(score) + "/6")

    if strength != "Strong":
        print("Suggestions:")
        for tip in suggestions(pwd):
            print("-", tip)


if __name__ == "__main__":
    main()