# Numerically integrate x/(1+x) from 1 to 3 using methods: midpoint, trapezoid, simpson for respective values of N => 5, 10, 25

from library import integrate_midpoint, integrate_trapezoid, integrate_simpson

def f(x):
    return x/(1+x)

# Midpoint method
sol1 = integrate_midpoint(f, [1,3], 20)

# Trapezoid method
sol2 = integrate_trapezoid(f, [1,3], 20)

# Simpson method
sol3 = integrate_simpson(f, [1,3], 27)

print(sol1, sol2, sol3)
