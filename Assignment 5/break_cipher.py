#-----------------------------------------
# To find matrix A and vector E
#-----------------------------------------

from utilities import *

ap = [[] for i in range(8)]
av = [[[] for i in range(8)] for j in range(8)]

#  For the diagonal elements
print("Finding Tuples..")
print("-"*50)
with open('inputs.txt', 'r') as input_file, open('outputs.txt', 'r') as output_file:
    for index, (inpline, outline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
        # Decode the blockwise characters, for block 1 extract block 1 chracters after converting them to byte
        inps = [DecodeBlock(msg)[index] for msg in inpline.strip().split(" ")]
        outs = [DecodeBlock(msg)[index] for msg in outline.strip().split(" ")]

        #  using (a_i,i(a_(i,i) ∗x^e_i )e_i )e_i to find tuples
        #  x - value of non-zero input block = ord(inp)
        #  a_(i,i) - diagonal element = j
        #  e_i - ith element of E = i
        for i in range(1, 127):
            for j in range(1, 128):
                flag = True
                for inp, outp in zip(inps, outs):
                    if ord(outp) != Exponentiate(Multiply(Exponentiate(Multiply(Exponentiate(ord(inp), i), j), i), j), i):
                        flag = False
                        break
                if flag:
                    ap[index].append(i)
                    av[index][index].append(j)

# printing tuples for each block
print("Tuples Found for all blocks")
tuple_blockwise=[[] for i in range(8)]
for block in range(8):
    for i, j in zip(av[block][block], ap[block]):
        tuple_blockwise[block].append((i,j))
    print(block, '\t', tuple_blockwise[block])

print("-"*50)

print("Finding other elements of the matrix A and vector E")
with open('inputs.txt', 'r') as input_file, open('outputs.txt', 'r') as output_file:
    for index, (inpline, outline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
        if index > 6 :
            continue
        inps = [DecodeBlock(msg)[index] for msg in inpline.strip().split(" ")]
        outs = [DecodeBlock(msg)[index+1] for msg in outline.strip().split(" ")]
        for i in range(1, 128):
            for p1, e1 in zip(ap[index+1], av[index+1][index+1]):
                for p2, e2 in zip(ap[index], av[index][index]):
                    flag = True
                    for inp, outp in zip(inps, outs):
                        if ord(outp) != Exponentiate(Add(Multiply(Exponentiate(Multiply(Exponentiate(ord(inp), p2), e2), p2), i) ,Multiply(Exponentiate(Multiply(Exponentiate(ord(inp), p2), i), p1), e1)), p1):
                            flag = False
                            break
                    if flag:
                        ap[index+1] = [p1]
                        av[index+1][index+1] = [e1]
                        ap[index] = [p2]
                        av[index][index] = [e2]
                        av[index][index+1] = [i]

for index in range(6):
    offset = index+2

    p_key = [e[0] for e in ap]
    lin_key = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            lin_key[i][j] = 0 if len(av[i][j]) == 0 else av[i][j][0]

    with open("inputs.txt", 'r') as inp, open("outputs.txt", 'r') as out:
        for index, (inpline, outline) in enumerate(zip(inp.readlines(), out.readlines())):
            if index > 7-offset:
                continue
            inps = [DecodeBlock(msg) for msg in inpline.strip().split(" ")]
            outs = [DecodeBlock(msg) for msg in outline.strip().split(" ")]
            for i in range(1, 128):
                lin_key[index][index+offset] = i
                flag = True
                for im, om in zip(inps, outs):
                    if Lin_Exponent_Encrypt(im, lin_key, p_key)[index+offset] != ord(om[index+offset]):
                        flag = False
                        break
                if flag:
                    av[index][index+offset] = [i]
                    break

lin_key = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lin_key[i][j] = 0 if len(av[i][j]) == 0 else av[i][j][0]


print("Found Matrix A")
print("A^T = ")
for i in range(8):
    print(lin_key[i])
print("-"*25)
print("Found Vector E")
print(p_key)
print("-"*50)
