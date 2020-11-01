import sys
from conversions import string_get_blocks, int_get_blocks, get_string, get_int
import rsa
import random
from math import factorial

def encrypt(plaintext, y, g, p, k):
    block_size = len(str(p)) // 4
    plaintext = string_get_blocks(plaintext, block_size)
    block_ciphertext = []

    for blok in plaintext:
        a = pow(g, k, p)
        b = pow(y, k) * blok % p
        block_ciphertext.append([a, b])

    ciphertext = block_ciphertext

    return ciphertext

def decrypt(ciphertext, x, p):
    block_size = len(str(p)) // 4
    block_plaintext = []

    for blok in ciphertext:
        a = blok[0]
        b = blok[1]
        a2 = pow(a, (p-1-x), p)
        m = b * a2 % p
        block_plaintext.append(m)

    plaintext = get_string(block_plaintext)

    return plaintext

def get_keys(g, x, p):
    if is_key_valid(g, x, p):
        return [(pow(g, x, p)), g, p], [x, p] # public key [y, g, p], private key [x, p]
    else:
        return 0

def is_key_valid(g, x, p):
    return (rsa.is_prime(p)) and (g < p) and (1 <= x) and (x <= p-2)

def is_k_valid(k, p):
    return (k < p) and (k >= 0)
    

# keys = get_keys(1795041, 119, 2792099)
# public_key = keys[0]
# private_key = keys[1]

# y = public_key[0]
# g = public_key[1]
# p = public_key[2]
# k = 123
# x = private_key[0]
# msg = "halo apa kabar? nama saya elvina".encode('latin-1')

# print(g, k, p)
# print(g**k)
# print((g**k) % p)

# ciphertext = encrypt(msg, y, g, p, k)
# print(ciphertext)

# plaintext = decrypt(ciphertext, x, p)
# print(plaintext)

# x = 2792097
# while rsa.is_prime(x) == False:
#     x += 1
# print(x)