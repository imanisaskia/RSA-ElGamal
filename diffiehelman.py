def get_our_key(n, g, x, y): 
    Y = get_my_key(n, g, y)
    return pow(Y, x, n)

def get_my_key(n, g, x):
    return pow(g, x, n)

# print(get_our_key(97, 5, 36, 58))