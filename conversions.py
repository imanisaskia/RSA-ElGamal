from math import gcd

def strToByte(s):
	return bytearray(s, "latin-1")

def byteToStr(b):
	return b.decode('latin-1')

def intToByte(i):
    return i.to_bytes((i.bit_length() + 7) // 8, 'big')

def byteToInt(b):
    return int.from_bytes(b, "big")

def get_blocks(message, n):
    msg_bytes = str(byteToInt(strToByte(message)))
    size = len(str(n)) - 1
    return [int(msg_bytes[i : i + size]) for i in range(0, len(msg_bytes), size)]

print(get_blocks("HELLO ALICE", 105))