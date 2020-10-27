import matplotlib.pyplot as plt
from library import monte_carlo

def f(x):
    return 4/(1+x**2)

answer = monte_carlo(f, [0.0, 1.0], 10)
print(answer)
