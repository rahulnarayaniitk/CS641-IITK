#-------------------------------------------------------------------
# To decrypt password using brut force by traversing all the inputs
#-------------------------------------------------------------------


from get_inp_out import conn_to_server, get_cip

padded_decrypted_pwd = ""
io = conn_to_server()
encrypted_pw = get_cip('password', io)  # ijmrgggglsihgsmlmtknhgfhhpgohqmu

for i in range(2):
    # Taking both the halves of the encrypted password
    encrypted_str = encrypted_pw[i*16:(i+1)*16]
    plain_str = ['f'] * 16
    print("Analyzing block "+str(i+1)+" of the Password : ", encrypted_str)
    for j in range(8):
        print("For Pair : ", j)
        for k in range(256):
            plain_str[j*2] = chr(ord('f') + (k >> 4))
            plain_str[(j*2) | 1] = chr(ord('f') + (k & 0xf))
            cipher_str = get_cip((''.join(plain_str)), io)
            # When block characters of the password and encrypted  match
            if cipher_str[j*2:(j+1)*2] == encrypted_str[j*2:(j+1)*2]:
                break
        padded_decrypted_pwd += chr(((ord(plain_str[j*2])-ord('f')) << 4) + (
            ord(plain_str[(j*2) | 1]) - ord('f')))
        if i == 0:
            print(padded_decrypted_pwd[:j+1])
        else:
            print(padded_decrypted_pwd[:j+1+8])

print("Padded Decrypted Password ", padded_decrypted_pwd)

for i in range(len(padded_decrypted_pwd)):
    if padded_decrypted_pwd[i] == '0':
        break

print("Password : ", padded_decrypted_pwd[:i])
