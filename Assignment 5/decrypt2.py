#--------------------------------------------------
# To decrypt password using matrix A and vector E
#--------------------------------------------------

from utilities import *

LINEAR_KEY_TRANS = [
    [84, 124, 13, 102, 100, 24, 10, 77],
    [0, 70, 28, 22, 38, 38, 119, 8],
    [0, 0, 43, 13, 0, 28, 23, 82],
    [0, 0, 0, 12, 117, 32, 101, 26],
    [0, 0, 0, 0, 112, 100, 25, 23],
    [0, 0, 0, 0, 0, 11, 94, 67],
    [0, 0, 0, 0, 0, 0, 27, 10],
    [0, 0, 0, 0, 0, 0, 0, 38]
]


EXPONENT_KEY = [18, 115, 40, 69, 90, 41, 25, 18]


password1 = "ijmrgggglsihgsml"
password2 = "mtknhgfhhpgohqmu"


def DecryptPassword(password):
    paswd = DecodeBlock(password)
    prev = ""
    for ind in range(8):
        for ans in range(128):
            inp = prev + EncodeChar(chr(ans))+(16-len(prev)-2)*'f'
            if ord(paswd[ind]) == Lin_Exponent_Encrypt(DecodeBlock(inp), LINEAR_KEY_TRANS, EXPONENT_KEY)[ind]:
                prev += EncodeChar(chr(ans))
                break
    return prev


print("Analyzing password for first block of the encrypted password : ", password1)
p1 = DecodeBlock(DecryptPassword(password1))
print("Decrypted Password : ", p1)
print("Analyzing password for second block of the encrypted password : ", password2)
p2 = DecodeBlock(DecryptPassword(password2))
print("Decrypted Password : ", p2)
padded_decrypted_pwd = p1+p2
print("Padded Decrypted Password : ", padded_decrypted_pwd)

for i in range(len(padded_decrypted_pwd)):
    if padded_decrypted_pwd[i] == '0':
        break

print("Password : ", padded_decrypted_pwd[:i])
