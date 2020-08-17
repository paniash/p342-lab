# Create two 3x3 matrices M and N in two separate files and read them to find MxA and MxN.

a = [1,4,9]  # vector A
with open('mpy.txt', 'r') as f:
    m = [[int(num) for num in line.split(',')] for line in f]

with open('npy.txt', 'r') as f:
    n = [[int(num) for num in line.split(',')] for line in f]

print("M =", m)
print("N =", n)
print("A =", a)

# calculating M x N
prod = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            prod[i][j] += m[i][k]*n[k][j]

print("M x N =", prod)  # displays M x N

# calculating M x A
vec = [0, 0, 0]
for i in range(3):
    for k in range(3):
        vec[i] += m[i][k] * a[k]

print("M x A =", vec)
