from math import gcd
from random import shuffle
from conversions import string_get_blocks, int_get_blocks, get_string, get_int

def is_coprime(a, b):
    return gcd(a, b) == 1

def is_prime(num):
    if num > 1:
        for i in range(2, num): 
            if (num % i) == 0: 
                return False
        else:
            return True 
    else:
        return False

def random_e(phi):
    suggestions = list(range(2, phi))
    shuffle(suggestions)
    for num in suggestions:
        if (gcd(num, phi)==1):
            return num

# Generate private and public keys, returns n, e, and d
def generate_keys(p, q, e = None):
    
    if not is_prime(p):
        print("Fail to generate keys;", p, "is not a prime number")
        return
    
    if not is_prime(q):
        print("Fail to generate keys;", q, "is not a prime number")
        return
    
    n = p * q
    phi = (p-1) * (q-1)

    if e:
        if not is_coprime(e, phi):
            print("Fail to generate keys;", e, "is not a co-prime of", phi)
            return
    else:
        e = random_e(phi)

    # generate private key
    k = 1
    d = (1 + k*phi) / e
    while not float.is_integer(d):
        k += 1
        d = (1 + k*phi) / e
    d = round(d)

    return n, e, d

def encrypt(plaintext, n, e):
    block_size = len(str(n)) // 4
    blocks = string_get_blocks(plaintext, block_size)
    c_blocks = []
    for block in blocks:
        c_blocks.append(pow(block, e, n))
    ciphertext = get_int(c_blocks, len(str(n)))
    return ciphertext

def decrypt(ciphertext, n, d):
    block_size = len(str(n))
    blocks = int_get_blocks(ciphertext, block_size)
    p_blocks = []
    for block in blocks:
        p_blocks.append(pow(block, d, n))
    plaintext = get_string(p_blocks)
    return plaintext

'''n, e, d = generate_keys(3109, 7331)
print(n)
print(e)
print(d)'''

c = encrypt(("TEST MESSAGE").encode('latin-1'), 22792079, 11378501)
print("Hasil:", c)
print(decrypt(c, 22792079, 18669701).decode('latin-1'))