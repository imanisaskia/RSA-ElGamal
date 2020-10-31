def strToByte(s):
	return bytearray(s, "latin-1")

def byteToStr(b):
	return b.decode('latin-1')

def intToByte(i):
    return bytes(i)

def byteToInt(b):
    return int.from_bytes(b, "big")

def int_blocks(i, n):
    i = str(i)
    blocks = []
    while not (i == ""):
        digits = 1
        block = i[0]
        i = i[1:]

        less = True

        while less and not (i == ""):
            new_block = block + i[0]
            if (int(new_block) < n):
                digits += 1
                block = new_block
                i = i[1:]
            else:
                less = False

        blocks.append(block)

    return blocks

print(int_blocks(byteToInt(strToByte("HELLO ALICE")), 105))