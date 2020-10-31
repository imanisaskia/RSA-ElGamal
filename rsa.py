from math import gcd
from random import shuffle
from conversions import get_blocks, get_string

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
    blocks = get_blocks(plaintext, block_size)
    print(blocks)
    c_blocks = []
    for block in blocks:
        c_blocks.append((block ** e) % n)
    ciphertext = get_string(c_blocks)
    return ciphertext

#n, e, d = generate_keys(3109, 7331)
#print(n)
#print(e)
#print(d)

c = encrypt("TEST MESSAGE", 3337, 79)
print(c)
print(encrypt(c, 3337, 1019))