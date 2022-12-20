value = 0b11010111

def swap(byte):
    left_nibble = byte & 0x0F
    right_nibble = byte >> 4
    swaped = (right_nibble<<4)|left_nibble

    print(bin(swaped))


swap(value)