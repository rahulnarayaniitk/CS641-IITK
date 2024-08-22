def euclidean_gcd(m, n):
    if m == 0:
        return (0, 1)
    else:
        x, y = euclidean_gcd(n % m, m)
        return (y - (n//m) * x, x)


(a,x) = (429,431955503618234519808008749742)
(b,y) = (1973,176325509039323911968355873643)
(c,z) = (7596,98486971404861992487294722613)
p = 455470209427676832372575348833

# Powers of g = (m=a-b and n=c-b)
m = b-a
n = c-b
print("m = ", m ,"and n = ", n)

# Using Extended Euclidean theorem, we got i and j such that mi+nj=1
i, j = euclidean_gcd(m, n)
print("i = ", i ,"and j = ", j)

x_inverse, _ = euclidean_gcd(x, p)
y_inverse, _ = euclidean_gcd(y, p)
z_inverse, _ = euclidean_gcd(z, p)
print("x_inverse = ", x_inverse ,", y_inverse = ", y_inverse, "and z_inverse = ", z_inverse)

#i is positive and j is negative
g = (pow(x_inverse, i, p)*pow(y, i-j, p)*pow(z_inverse, -1*j, p))%p
print("g = ", g)

g_inverse, _ = euclidean_gcd(g, p)
print("g_inverse = ", g_inverse)

password = (x * pow(g_inverse, a, p))%p
print("password = ", password)


# Output
# m =  1544 and n =  5623
# i =  -2298 and j =  631
# x_inverse =  70749996790223471732904681640 , y_inverse =  -226523059948924229766221663708 and z_inverse =  105171748371597409614445194812
# g =  52565085417963311027694339
# g_inverse =  -68963777479288598328997449380
# password =  134721542097659029845273957

