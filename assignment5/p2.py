from library import polynomial_solver

# def f(x, coeffs = [1, -3, -7, 27, -18]):
#     return polynomial(x, coeffs)

roots = polynomial_solver([-3, 3, 0, -4], 1, 1e-6)
print(roots)
