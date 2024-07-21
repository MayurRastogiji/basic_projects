import random
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
lst = [i for i in range(9999) if prime(i)]
# print(lst)
p = random.choice(lst)
q = random.choice(lst)
while p == q:
    q = random.choice(lst)
# print(p, q)
n = p * q
phi_n = (p - 1) * (q - 1)
e = random.choice([i for i in range(2, 1000) if prime(i) and phi_n % i != 0])
# print(e)
# e = random.choice(e_lst)
for i in range(2, phi_n):
    if (e * i) % phi_n == 1:
        d = i
        break
plain_text = input("Enter the plain text: ")
m = [format(ord(i), '08b') for i in plain_text]
print(m)
m_e = ''.join(m)
c = pow(int(m_e, 2), e)%n
print("Encrypted text: ", c)
m = pow(c, d)%n
if (m == m_e):
    print("success")
m = format(m, 'b')
print(m)
print("decrypted_text is :")
for i in range(0, len(m), 8):
    print(chr(int(m[i:i+8], 2)), end='')
# print(c, type(c))
