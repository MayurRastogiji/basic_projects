import random as rm
from cryptography.fernet import Fernet
n = input("Enter your Name :\n")
print ("Hello ",n,"\nWelcome to my World of Encryption:\n")


def encrypt_r():
                string = str(input("Enter your text  :\n"))
                result = ''
                for i in string:
                    if 'a' <= i <= 'z':
                        transformed_str= chr(ord('a') + ord('z') - ord(i))    
                    elif 'A' <= i <= 'Z':
                        transformed_str = chr(ord('A') + ord('Z') - ord(i)) 
                    else:
                        transformed_str = i
                    result += transformed_str
                return result

key = Fernet.generate_key()

def encrypt_cf(key):
    text = str(input("Enter your text to be encrypted :\n"))
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text
def decrypt_cf(key):
    encrypted_text = str(input("Enter your text to be decrypted :\n"))
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text



def encrypt_k():
    temp_result = ''
    salt = ''
    string = str(input("Enter your text to be encrypted :\n"))
    key = int(input("Enter your symmetric key(in integer) for encryption."))
    for i in string:
        if 'a' <= i <= 'z':
            temp = ord(i) % 96
            transformed_str= chr(((temp + key - 1) % 26) + 97)
        elif 'A' <= i <= 'Z':
            temp = ord(i) % 64
            transformed_str= chr(((temp + key - 1) % 26) + 65)
        else:
            salt += i
            transformed_str = i
            
        temp_result += transformed_str
        result = salt+temp_result+salt
    return result
def decrypt_k():
    temp_result = ''
    salt = ''
    string = str(input("Enter your text to be decrypted :\n"))
    key = int(input("Enter your symmetric key(in integer) for decryption."))
    for i in string:
        if 'a' <= i <= 'z':
            temp = ord(i) % 96
            transformed_str= chr(((temp - key +25) % 26) + 97)
        elif 'A' <= i <= 'Z':
            temp = ord(i) % 64
            transformed_str= chr(((temp - key +25) % 26) + 65)
        else:
            salt += i
            transformed_str = i
        temp_result += transformed_str
        len_salt = len(salt)/3
        if int(len_salt) == 0:
            result = temp_result
        else:
            result = temp_result[int(len_salt):-(int(len_salt))]
    return result



def encrypt_rm():
    result = ''
    string = str(input("Enter your text to be encrypted :\n"))
    temp_lst = string.split(' ')
    for i in temp_lst:
        length = len(i)
        for i in range(length):
            inte = rm.random() * 100
            if inte != 58 and 46:
                result += chr(int(inte))
    key = ''
    for i in string:
        if i == ' ':
            key += chr(58)
            continue
        else:
            key += str(ord(i))
        key += chr(46)
    return result, key
def decrypt_rm():
    result = ''
    inte = 0
    string = str(input("Enter your text to be decrypted :\n"))
    key = str(input("Enter your key for decryption that is generated dunring encryption:\n"))   
    for i in key:
        if i == ':':
            result += ' '
        elif i == '.':
            result += chr(inte)
            inte = 0
            continue
        else:
            inte = inte * 10 + int(i)       
    return result



def while_true(p):
    
    dic_encrypt = {
        '26.RV.10' : encrypt_r,
        '17.CF.11' : encrypt_cf,
        '09.k.06' : encrypt_k,
        '19.RM.06' : encrypt_rm,
    }
    dic_decrypt = {
        '26.RV.10' : encrypt_r,
        '17.CF.11' : decrypt_cf,
        '09.k.06' : decrypt_k,
        '19.RM.06' : decrypt_rm,
    }
    while True:
        ch = int(input("Enter 1 for encryption\nEnter 2 for decryption\nEnter 3 for exit this encryption mode\n"))
        if ch == 1:
            while True:  
                if p == '17.CF.11':
                    print(dic_encrypt[p](key))
                else:
                    print(dic_encrypt[p]())
                ch1 = str(input("Do you want to continue ? (y/n)"))
                if ch1 == "y":
                    continue
                else:
                    break
        elif ch == 2:
            while True:
                if p == '17.CF.11':
                    print(dic_decrypt[p](key))
                else:
                    print(dic_decrypt[p]())
                ch2 = str(input("Do you want to continue ? (y/n)"))
                if ch2 == "y":
                    continue
                else:
                    break
        elif ch == 3:
            print (f"Thanks ({n}) for using this Encryption mode.")
            break



def check(num):
    decimal = 0
    integer = 0
    i = 0
    if check_decimal(num) == False:
        print("It is an integer")
        exit()
    else:
        try:
            while(num[i] != "."):
                integer = integer + int(num[i])
                i += 1
        except:
            pass
        if num[i] == ".":
            i += 1
        for k in range(i,len(num)):
            decimal = decimal + int(num[k])
        if integer == decimal:
            return True
        else:
            return False
        
def check_decimal(num):
    if "." in num:
        return True
    else:
        return False
    
# if(check("123.15")):
#     print("Equal")
# else:
#     print("not equal")

skip = 0
while True:
    while skip%3 == 0:
        print("\n\nThis is small verification test to check whether you are a human or not. \nPlease enter a decimal number to check. \nIf the sum of the integer part and the decimal part of the number is equal, then you are a human. \nOtherwise, you are not a human.\n\n")
        num = input("Enter a decimal number to check: ")
        # print(type(num))
        if check(num):
            print("YOU ARE A VERIFIED HUMAN. \nYou are allowed to use my encryption mode.\n")
        else:
            print("WE ARE UNABLE TO VERIFY YOU AS A HUMAN.")
            exit()
        skip += 1
    skip += 1
    p = str(input("Enter 'given key' for using your encryption mode\nNOTE: if you don't have key ask it from creater of this program\nEnter 0 for exit program\n"))
    if p == "15.MC.10":
        print ("Access Granted to encryption mode M\n")
        dic = {
        'a' : '\._/',
        'b' : '\_.../',
        'c' : '\_._./',
        'd' : '\_../',
        'e' : '\./',
        'f' : '\.._./',
        'g' : '\__./',
        'h' : '\..../',
        'i' : '\../',
        'j' : '\.___/',
        'k' : '\_._/',
        'l' : '\._../',
        'm' : '\__/',
        'n' : '\_./',
        'o' : '\___/',
        'p' : '\.__./',
        'q' : '\__._/',
        'r' : '\._./',
        's' : '\.../',
        't' : '\_/',
        'u' : '\.._/',
        'v' : '\..._/',
        'w' : '\.__/',
        'x' : '\_.._/',
        'y' : '\_.__/',
        'z' : '\__../',
        '1' : '\.____/',
        '2' : '\..___/',
        '3' : '\...__/',
        '4' : '\...._/',
        '5' : '\...../',
        '6' : '\_..../',
        '7' : '\__.../',
        '8' : '\___../',
        '9' : '\____./',
        '0' : '\_____/',
        'A' : ':._:',
        'B' : ':_...:',
        'C' : ':._.:',
        'D' : ':_..:',
        'E' : ':.:',
        'F' : ':.._.:',
        'G' : ':__.:',
        'H' : ':....:',
        'I' : ':..:',
        'J' : ':.___:',
        'K' : ':_._:',
        'L' : ':._..:',
        'M' : ':__:',
        'N' : ':_.:',
        'O' : ':___:',
        'P' : ':.__.:',
        'Q' : ':__._:',
        'R' : ':._.:',
        'S' : ':...:',
        'T' : ':_:',
        'U' : ':.._:',
        'V' : ':..._:',
        'W' : ':.__:',
        'X' : ':_.._:',
        'Y' : ':_.__:',
        'Z' : ':__..:',
        '!' : ':_._._:',
        '?' : ':..__.:',
        }
        dic1 = {v:k for k,v in dic.items()}
        while True:
            ch = int(input("Enter 1 for encryption\nEnter 2 for decryption\nEnter 3 for exit this encryption mode\n"))
            if ch == 1:
                while True:
                    en = str(input("Enter your text to be encrypted :\n"))
                    en1 = en
                    for old,new in dic.items():
                        en1 = en1.replace(old,new)
                    print(en1)
                    ch1 = str(input("Do you want to continue ? (y/n)"))
                    if ch1 == "y":
                        continue
                    else:
                        break
            elif ch == 2:
                while True:
                    de = str(input("Enter your text to be decrypted :\n"))
                    de1 = de
                    for old1,new1 in dic1.items():
                        de1 = de1.replace(old1,new1)
                    print(de1)
                    ch2 = str(input("Do you want to continue ? (y/n)"))
                    if ch2 == "y":
                        continue
                    else:
                        break
            elif ch == 3:
                print (f"Thanks ({n}) for using this Encryption mode.")
                break   



    elif p == '26.RV.10':
        print("Access Granted to encryption mode R")
        while_true(p)
    


    elif p == '17.CF.11':
        print("Access Granted to encryption mode F")
        while_true(p)



    elif p == '09.k.06':
        print("Access Granted to encryption mode k th place. currently working only for capital letters")
        while_true(p)
    


    elif p == '19.RM.06':
        print("Access Granted to encryption mode RM")
        while_true(p)


            
    elif p == '0':
        print(f"Thanks {n} for using my encryptions\nhope you enjoyed it")
        exit()

        
    else:
        print ("Access Denied\n")
        exit()


# next algorithm is to create plain text only using random function and also create key while encrypting and decrypting