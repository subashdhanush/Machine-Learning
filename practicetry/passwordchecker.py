def check_password_strength(pwd):
    import re
    if (len(pwd) >= 8 and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[a-z]", pwd) and
        re.search(r"[0-9]", pwd) and
        re.search(r"[!@#$%^&*()_+]", pwd)):
        return "Strong"
    return "Weak"

print(check_password_strength("Hello123"))  # Strong
