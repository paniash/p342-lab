# To create two vectors of type A=(a1, a2, a3) and B=(b1, b2, b3) with numbers as input. Find A+B and A.B
A = [1, 4, 9]
B = [2, 17, 26]

add = []  # A+B

for i in range(3):
    add.append(A[i]+B[i])

prod = 0
for j in range(3):
    prod += A[j]*B[j]

print("Sum:",add)
print("Dot product:", prod)
