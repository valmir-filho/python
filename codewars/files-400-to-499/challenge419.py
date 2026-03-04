"""
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)

The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
"""


def data_reverse(data):
    # Divide em blocos de 8 bits.
    bytes_list = [data[i:i+8] for i in range(0, len(data), 8)]
    
    # Inverte a ordem dos blocos.
    bytes_list.reverse()
    
    # Junta tudo novamente em uma única lista.
    return [bit for byte in bytes_list for bit in byte]
