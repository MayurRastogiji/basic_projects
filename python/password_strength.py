i = 0
z = 0
speacial_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while(i == 0):
    password = input("Enter a password: ")
    print("Case 1: Password must be at least 8 characters long")
    if len(password) < 8 :
        print("case fails : \033[91m\u2718\033[0m")
        print("Password is too short")
    elif len(password) > 16:
        print("case fails : \033[91m\u2718\033[0m")
        print("Password is too long")
    else:
        print("case pass : \033[92m\u2714\033[0m")
        z = 1
        print("Case 2: Password must contain at least one special character")
        for c in speacial_characters:
            if c in password and z == 1:
                print("case pass : \033[92m\u2714\033[0m")
                z = 2
                print("Case 3: Password must contain at least one number")
                for n in numbers:
                    if n in password and z == 2:
                        print("case pass : \033[92m\u2714\033[0m")
                        z = 3
                        print("Case 4: Password must contain at least one upper case letter")
                        for u in upper_case:
                            if u in password and z == 3:
                                print("case pass : \033[92m\u2714\033[0m")
                                z = 4
                                print("Case 5: Password must contain at least one lower case letter")
                                for l in lower_case:
                                    if l in password and z == 4:
                                        print("case pass : \033[92m\u2714\033[0m")
                                        z = 5
                                        print("Password is \033[32mVery Strong\033[0m")
                                        i = 1
                                        exit()
                                    elif (l == lower_case[-1] and z < 5):   
                                        print("case fails : \033[91m\u2718\033[0m")
                                        print("Password does not contain any lower case letters")
                                        print("Password is \033[92mStrong\033[0m")
                                        break
                            elif (u == upper_case[-1] and z < 4):
                                print("case fails : \033[91m\u2718\033[0m")
                                print("Password does not contain any upper case letters")
                                print("Password is \033[93mGood\033[0m")
                                break
                    elif(n == numbers[-1] and z < 3):
                        print("case fails : \033[91m\u2718\033[0m")
                        print("Password does not contain any numbers")
                        print("Password is \033[38;5;214mAverage\033[0m")
                        break
            elif (c == speacial_characters[-1] and z < 2):
                print("case fails : \033[91m\u2718\033[0m")
                print("Password does not contain any special characters")
                print("Password is \033[91mWeak\033[0m")
                break