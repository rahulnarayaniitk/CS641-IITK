

x = "20 21 44 68 59 82 20 50 30 28 38 51 56 50 117 67 75 35 121 6 96 126 102 93 126 60 39 116 103 29 18 91"
e = [0 for i in range(32)]
# p range 1-32
p = x.split(" ")
p = [int(x) for x in p]
p0 = int(p[0])
p = p[1:]
e[0] = 1

for k in range(1, len(p)):
    sum_ = 0
    for i in range(k):
        if k > p0:
            sum_ += 0
        else:
            sum_ += (pow(-1, i) * e[k-i-1] * p[i])
    # using inverse modulo based on fermat's little theorem
    sum_ = sum_*(k**125)
    sum_ = sum_ % 127
    e[k] = sum_

e_20 = e[0:21]
print("e_20 :", e_20)

# Letters of the password
letters = []
for letter in range(102, 118):
    x = 0
    for i in range(0, 32):
        x = x + ((-1)**(i))*e[i]*(letter**(32-i-1))
        x = x % 127
    if(x == 0):
        letters.append(letter)

print("Password Letters in ASCII :", letters)

pass_char = [chr(i) for i in letters]
# All letters used in password
print("Password Letters :", pass_char)

# Matrix of power of characters used
pow_char = [[0 for i in range(12)] for j in range(12)]
power_sum = [p[i] for i in range(12)]

for j in range(12):
    for i, ch in enumerate(letters):
        pow_char[j][i] = (ch**(j+1)) % 127

# Using both the above values to solve pow_char*X=power_sum in sage ( matrix solution)

# frequency found from the 'sage_frq.ipynb' when run in SAGE environment
freq = [1, 4, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1]

for i, j in zip(pass_char, freq):
    print(str(i)+":" + str(j))

print("Password is : ", end="")
for i, j in zip(pass_char, freq):
    for x in range(j):
        print(i, end="")
