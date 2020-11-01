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

# FUNC: GENERATE KEYS
# Generate private and public keys, returns message (if failed), n, e, and d
def generate_keys(p, q, e = None):
    if not is_prime(p):
        return ("Failed to generate keys; p is not a prime number"), 0,0,0
    if not is_prime(q):
        return ("Failed to generate keys; q is not a prime number"), 0,0,0

    # generate n    
    n = p * q
    if (n < 1000):
        return ("Failed to generate keys; n=" + str(n) + " must be > 1000"), 0,0,0
    phi = (p-1) * (q-1)

    if not (e == None):
        if not is_coprime(e, phi):
            return ("Failed to generate keys; e=" + str(e) + " is not co-prime of phi=" + str(phi)), 0,0,0
    else:
        # generate random e if not given
        e = random_e(phi)

    # generate d
    k = 1
    d = (1 + k*phi) / e
    while not float.is_integer(d):
        k += 1
        d = (1 + k*phi) / e
    d = round(d)

    return None, n, e, d

# FUNC: ENCRYPT
# Encrypt plaintext, returns ciphertext (integer string)
def encrypt(plaintext, n, e):
    block_size = len(str(n)) // 4
    blocks = string_get_blocks(plaintext, block_size)
    c_blocks = []
    for block in blocks:
        c_blocks.append(pow(block, e, n))
    ciphertext = get_int(c_blocks, len(str(n)))
    return ciphertext

# FUNC: DECRYPT
# Decrypt ciphertest (integer string), returns plaintext (string)
def decrypt(ciphertext, n, d):
    block_size = len(str(n))
    blocks = int_get_blocks(ciphertext, block_size)
    p_blocks = []
    for block in blocks:
        p_blocks.append(pow(block, d, n))
    plaintext = get_string(p_blocks)
    return plaintext

'''msg, n, e, d = generate_keys(5, 2, 1019)
if msg:
    print(msg)
else:
    print(n)
    print(e)
    print(d)'''

'''c = encrypt(("TEST MESSAGE").encode('latin-1'), 22792079, 11378501)
print("Hasil:", c)
print(decrypt(c, 22792079, 18669701).decode('latin-1'))'''