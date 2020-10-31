import sys
import conversions
import rsa
import random
from math import factorial

def encrypt(plaintext, g, x, p):
    plaintext = conversions.get_blocks(plaintext, p)
    block_ciphertext = []
    k = get_random_k(p)
    y = get_public_key(g, x, p)
    
    for blok in plaintext:
        a = (g**k) % p
        b = (y**k) * blok % p
        block_ciphertext.append(str(a) + str(b))

    byte_ciphertext = conversions.arr_to_str(block_ciphertext)
    # byte_ciphertext = [byte_ciphertext[i : i + 2] for i in range(0, len(byte_ciphertext), 2)]
    # ciphertext = conversions.byteToStr(byte_ciphertext)
    
    return byte_ciphertext

def decrypt(ciphertext, key):
    plaintext = ciphertext

    return plaintext

def get_public_key(g, x, p):
    return ((g**x) % p)

def is_key_valid(g, x, p):
    return (rsa.is_prime(p)) and (g < p) and (1 <= x) and (x <= p-2)

def get_random_k(p):
    return random.randrange(1, p-2)

# print(sys.maxsize, 2**63-1)
# for i in conversions.strToByte("halo"):
#     print(i)
# print(get_random_k(137))

print(encrypt("halo", 1, 2, 317))