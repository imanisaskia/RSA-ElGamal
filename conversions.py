def get_blocks(message, block_size):
    blocks = []
    for i in range(0, len(message), block_size):
        block = 0
        for j in range(block_size):
            if ((i+j) < len(message)):
                block = block * 10000 + ord(message[i+j])
        blocks.append(block)
    return blocks

def get_string(blocks):
    message = ''
    for i in range(len(blocks)):
        block_msg = ""
        while (len(str(blocks[i])) > 4):
            block_msg = chr(blocks[i] % 10000) + block_msg
            blocks[i] //= 10000
        block_msg = chr(blocks[i]) + block_msg
        message += block_msg
    return message

#blocks = get_blocks("HELLO ALICE", 1)
#print(blocks)

#msg = get_string(blocks)
#print(msg)