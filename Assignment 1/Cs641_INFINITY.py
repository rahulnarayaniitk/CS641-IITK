mapping = ['g', '#', 'e', 'm', 'f', 't', 'o', 'a', 'h', 'p', 's', 'w',
           'r', 'b', 'i', 'c', 'n', 'y', 'v', '#', 'l', 'u', '#', 'q', 'd', '#']

alphabets = [chr(i+ord('a')) for i in range(26)]
print(alphabets)
print(mapping)

print(len(mapping))

key = [(c[0], c[1]) for c in zip(alphabets, mapping)]
for k in key:
    print(str(k[0])+"=>" + str(k[1]))

print(key)


def decrypt(cipherText):
    cipherText = [c for c in list(cipherText.lower())]
    ans = ""
    for c in list(cipherText):
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            c = mapping[ord(c)-ord('a')]
        ans += c

    print(''.join(ans))


cipher_text = "omkf pi hdn cmgef icphsck .H krg vphqkc c,fic mco kqgf ioqag eo qfcmckf oq ficpihdncm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmcoqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yegmfio kdck kha cokh kodjuck vn k fofvfogqpojicmoqli opiyoa of kihsc nccqki oefcynr2 juhpck. Fi c jhkklgm yok oMxr9V1x yaflofigvffic xvgfck. Fio kokfice"
decrypt(cipher_text.replace(" ", ""))


cipher_adjusted_space = "Fiok ok fic eomkf pihdncm ge fic phsck .Hk rgv phq kcc,ficmc ok qgfioqa ge oqfcmckf oq fic pihdncm .Kgdc ge fic uhfcm pihdncmk louu nc dgmc oqfcmckfoqa fihq fiok gqc!Fic pgyc vkcy egm fiok dckkhac ok h kodjuc kvnkfofvfogq pojicm oq liopi yoaofk ihsc nccq kioefcy nr 2 juhpck. Fic jhkklgmy ok oMxr9V1xyaf lofigvf fic xvgfck."
decrypt(cipher_adjusted_space)
