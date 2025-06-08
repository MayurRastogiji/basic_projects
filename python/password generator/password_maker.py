import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special = '!@#$%^&*()-_=+[]{}|;:,.<>?'
letter = lower + upper + digits + special
def Spassword_new(): 
    password = ''.join(random.choice(random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)) for _ in range(8))
    print("Generated Password:", password)
    if check(password):
        return password
    else:
        return Spassword_new()
def check(password):
    return (
        len(password) >= 8 and
        any(c.isdigit() for c in password) and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c in special for c in password)
    )

def Spassword_update(old_password):
    while not check(old_password):
        half = len(old_password) // 2
        passw1 = old_password[:half]
        passw2 = old_password[half:]
        parts = [passw1, passw2]

        if not any(c in special for c in old_password):
            parts.append(random.choice(special))

        if not any(c.isdigit() for c in old_password):
            parts.append(random.choice(digits))

        if not any(c.isupper() for c in old_password):
            parts.append(random.choice(upper))

        if not any(c.islower() for c in old_password):
            parts.append(random.choice(lower))

        if len(old_password) < 8:
            extra = 8 - len(old_password)
            parts.extend(random.choice(letter) for _ in range(extra))

        random.shuffle(parts)
        old_password = ''.join(parts)

    return old_password
if __name__ == "__main__":
    Spassword_new()