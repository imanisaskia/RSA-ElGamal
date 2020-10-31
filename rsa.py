from math import gcd
from random import shuffle

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
def generate_keys(p, q, e = None, pub_fpath = "key.pub", pri_fpath = "key.pri"):
    
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

    # write public key in format n<br>e
    f = open(pub_fpath, "w")
    f.write(str(n) + "\n" + str(e))
    f.close()
    print("Public key saved to", pub_fpath)

    # generate private key
    k = 1
    d = (1 + k*phi) / e
    while not float.is_integer(d):
        k += 1
        d = (1 + k*phi) / e
    d = round(d)

    # write private key
    f = open(pri_fpath, "w")
    f.write(str(d))
    f.close()
    print("Private key saved to", pri_fpath)

    return n, e, d

n, e, d = generate_keys(2, 5, 3)
print("n:", n)
print("e:", e)
print("d:", d)
