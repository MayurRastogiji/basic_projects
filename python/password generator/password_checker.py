from termcolor import colored
from password_maker import Spassword_update, Spassword_new


def update():
    a = input("To update your password Type 'Update'\nTo Generate new Strong Password Via Computer Type 'new'\nElse Type 'Exit'\n")
    if a == "Exit":
        print("Exiting the program.......")
        exit()
    if a == "Update":
        print(Spassword_update(password))
    elif a == "new":
        print(Spassword_new())

password = input("Enter Your Password: \n")
# print("Your Password is: ", password)
strength = 0
if len(password) < 8:
    print("\033[91m✖\033[0m Password must be at least 8 characters long.")
else:
    print("\033[92m✔\033[0m Password length is valid.")
    strength += 1
if not any(char.isdigit() for char in password):
    print("\033[91m✖\033[0m Password must contain at least one digit.")
else:
    print("\033[92m✔\033[0m digit found in password.")
    strength += 1
if not any(char.isupper() for char in password):
    print("\033[91m✖\033[0m Password must contain at least one uppercase letter.")
else:
    print("\033[92m✔\033[0m Password contains an uppercase letter.")
    strength += 1
if not any(char.islower() for char in password):
    print("\033[91m✖\033[0m Password must contain at least one lowercase letter.")
else:
    print("\033[92m✔\033[0m Password contains a lowercase letter.")
    strength += 1
if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
    print("\033[91m✖\033[0m Password must contain at least one special character.")
else:
    print("\033[92m✔\033[0m Password contains a special character.")
    strength += 1
print()
print("Test Case Passed: ", strength, "out of 5\n")
print()
match strength:
    case 0:
        print(colored("Not a single case passed. Something went wrong, \nCrossCheck your password.", "dark_grey"))
        update()
    case 1:
        print(colored("Your password is very weak.", "red"))
        update()
    case 2:
        print(colored("Your password is weak.", "light_grey"))
        update()
    case 3:
        print(colored("Your password is moderate.", "yellow"))
        update()
    case 4:
        print(colored("Your password is strong.", "blue"))
        update()
    case 5:
        print(colored("Your password is very strong.", "green"))
