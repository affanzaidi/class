rgb = 0xABCD


def conversion(rgb):
    r = (rgb >> 11)
    print(r)
    g = ((rgb >> 5)& 0x03F)
    print(g)
    b =(rgb )&  0x001F
    print(b)

    # r = r<<5
    # g = g<<6
    # b = b<<

    r = bin(((r*255)/31)<<16)
    g = bin(((g*255)/63)<<8)|r
    b = bin((b*255)/31)|g

    print(b)


conversion((rgb))