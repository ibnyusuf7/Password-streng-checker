Python
import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[@#$%^&*!]", password):
        score += 1

    if score == 5:
        return "STRONG"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "WEAK"


password = input("Enter password: ")
strength = check_password(password)

print("Password Strength:", strength)
