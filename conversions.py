from Crypto.Util.number import bytes_to_long, long_to_bytes

# from string (plaintext) to blocks of BigNum
def string_get_blocks(message, block_size):
    blocks = []
    for i in range(0, len(message), block_size):
        block = bytes_to_long(message[i:i+block_size])
        blocks.append(block)
    return blocks

# from integer string (ciphertext) to blocks of BigNum
def int_get_blocks(message, block_size):
    blocks = []
    for i in range(0, len(message), block_size):
        block = int(message[i:i+block_size])
        blocks.append(block)
    return blocks

# from blocks of BigNum to integer string (ciphertext)
def get_int(blocks, max_digits):
    int_string = ''
    for block in blocks:
        string = str(block)
        if (len(string) < max_digits):
            string = '0' * (max_digits - len(string)) + string
        int_string += string
    return int_string

# from blocks of BigNum to string (plaintext)
def get_string(blocks):
    message = long_to_bytes(blocks[0])
    for i in range(1, len(blocks)):
        block_msg = long_to_bytes(blocks[i])
        message += block_msg
    return message