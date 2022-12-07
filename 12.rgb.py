rgb = 0xffffff


def conversion(rgb):
    r = ((rgb >> 16)& 0xFF)
    g = ((rgb >> 8)& 0xFF)
    b = (rgb & 0xFF)

    # r = r>>3
    # g = g>>3
    # b = b>>2

    r = int((r*31)/255)
    g = int((g*31)/255)
    b = int((b*63)/255)

    reduced_bit = (r<<11)
    reduced_bit |= (g<< 6)
    reduced_bit |= b
    print(reduced_bit)


conversion(rgb)