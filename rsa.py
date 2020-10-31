from math import gcd

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

# Generate private and public keys, returns success (boolean)
def generate_keys(p, q, e, pub_fpath = "key.pub", pri_fpath = "key.pri"):
    if is_prime(p) and is_prime(q):
        n = p * q
        phi = (p-1) * (q-1)

        if is_coprime(e, phi):
            print("Public key: n =", n, "; e =", e)

            k = 1
            d = (1 + k*phi) / e
            while not float.is_integer(d):
                k += 1
                d = (1 + k*phi) / e
            d = round(d)
            print("Private key: d =", d)
            return True
        else:
            return False
    else:
        return False

generate_keys(47, 71, 79)