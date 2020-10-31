import sys
import conversions
import rsa
import random
from math import factorial

def encrypt(plaintext, g, x, p):
    plaintext = conversions.get_blocks(plaintext, p)
    ciphertext = plaintext

    return ciphertext

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