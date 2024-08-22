
GF128_MSB = 1 << 6
GF128_MASK = (1 << 7) - 1

multiply_c = [[-1]*128 for i in range(128)]
exponent_c = [[-1]*128 for i in range(128)]


def Add(elem1, elem2):
    elem1 = int(elem1)
    elem2 = int(elem2)
    return elem1 ^ elem2


def Multiply(elem1, elem2):
    if multiply_c[elem1][elem2] != -1:
        return multiply_c[elem1][elem2]
    elem1 = int(elem1)
    elem2 = int(elem2)
    elem3 = 0
    ind = 0
    for ind in range(7):
        elem3 <<= 1
        if (elem1 & GF128_MSB):
            elem3 = Add(elem3, elem2)
        elem1 <<= 1
    upper = elem3 >> 7
    product = Add(Add(upper, upper << 1), elem3 & GF128_MASK)
    multiply_c[elem1 >> 7][elem2] = product
    multiply_c[elem2][elem1 >> 7] = product
    return product


def Exponentiate(elem, power):
    if exponent_c[elem][power] != -1:
        return exponent_c[elem][power]
    result = 0
    if power == 0:
        result = 1
    elif power == 1:
        result = elem
    elif power % 2 == 0:
        sqrt_elem = Exponentiate(elem, power >> 1)
        result = Multiply(sqrt_elem, sqrt_elem)
    else:
        sqrt_elem = Exponentiate(elem, power >> 1)
        result = Multiply(sqrt_elem, sqrt_elem)
        result = Multiply(elem, result)
    exponent_c[elem][power] = result
    return result


def LinearTransform(matrix, elem_list):
    def addVector(v1, v2):
        result = [0]*8
        for ind, (elem1, elem2) in enumerate(zip(v1, v2)):
            result[ind] = Add(elem1, elem2)
        return result

    def scalarmultVector(v, scalar_elem):
        result = [0]*8
        for ind, elem in enumerate(v):
            result[ind] = Multiply(elem, scalar_elem)
        return result
    result = [0]*8
    for row, elem in zip(matrix, elem_list):
        result = addVector(scalarmultVector(row, elem), result)
    return result


def EncodeBlock(plain):
    if len(plain) != 8:
        assert False
    cipher = ""
    for ch in plain:
        cipher += EncodeChar(ch)
    return cipher


def EncodeChar(char):
    if ord(char) > 128:
        assert False
    hex_str = "{0:02x}".format(ord(char))
    fchar = chr(int(hex_str[0], 16) + ord('f'))
    schar = chr(int(hex_str[1], 16) + ord('f'))
    return fchar+schar


def DecodeChar(st):
    if len(st) != 2:
        assert False

    char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
    return char


def DecodeBlock(cipher):  # Takes two characters from each block - then find their number ff-0,fg-1,gf-16..., then return chr(num)
    if len(cipher) != 16:
        print(cipher)
        assert False
    plain = [DecodeChar(cipher[i:i+2]) for i in range(0, len(cipher), 2)]
    return "".join(plain)


def Lin_Exponent_Encrypt(plaintext, lin_key, exp_key):
    plaintext = [ord(c) for c in plaintext]
    CT = [[0 for j in range(8)] for i in range(8)]  # 8*8 Matrix of zeroes

    #  First Layer : Exponentiation
    for ind, elem in enumerate(plaintext):
        CT[0][ind] = Exponentiate(elem, exp_key[ind])

    #  Second Layer : Linear Transform
    CT[1] = LinearTransform(lin_key, CT[0])

    #  Third Layer : Exponentiation
    for ind, elem in enumerate(CT[1]):
        CT[2][ind] = Exponentiate(elem, exp_key[ind])

    #  Fourth Layer : Linear Transform
    CT[3] = LinearTransform(lin_key, CT[2])

    #  Fifth Layer : Exponentiation
    for ind, elem in enumerate(CT[3]):
        CT[4][ind] = Exponentiate(elem, exp_key[ind])

    return CT[4]
