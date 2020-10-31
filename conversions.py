from math import gcd

def strToByte(s):
	return bytearray(s, "latin-1")

def byteToStr(b):
	return b.decode('latin-1')

def intToByte(i):
    return bytes(i)

def byteToInt(b):
    return int.from_bytes(b, "big")

def get_blocks(message, n):
    msg_bytes = str(arr_to_str(strToByte(message)))
    size = get_block_size(n)
    return [int(msg_bytes[i : i + size]) for i in range(0, len(msg_bytes), size)]

def get_block_size(n):
    max_val = n-1
    size = 1
    while max_val > 9:
        max_val = max_val // 10
        size += 1
    return size

def arr_to_str(arr):
    try:
        return ''.join(str(e) for e in arr)
    except:
        return ''.join(arr)

# print(int_blocks(byteToInt(strToByte("HELLO ALICE")), 105))