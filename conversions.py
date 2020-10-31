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
    msg_int_string = str(byteToInt(strToByte(message)))
    size = len(str(n)) - 1
    return [int(msg_int_string[i : i + size]) for i in range(0, len(msg_int_string), size)]

def get_string(blocks, n):
    msg_int_string = ""
    size = len(str(n)) - 1
    for block in blocks:
        digits = len(str(block))
        msg_int_string += ('0' * (size - digits)) + str(block)
    return byteToStr(intToByte(int(msg_int_string)))

blocks = get_blocks("HELLO ALICE", 105)
print(blocks)

msg = get_string(blocks, 105)
print(msg)