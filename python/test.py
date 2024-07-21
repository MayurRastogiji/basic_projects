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

# result = encrypt_k()
# print(result)
result = decrypt_k()
print(result)
