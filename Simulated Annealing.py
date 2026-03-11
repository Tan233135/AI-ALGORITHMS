import random
import math

# Example objective function (maximize)
def f(x):
    return -(x - 5) ** 2 + 25

# Generate neighbor
def neighbor(x):
    return x + random.uniform(-1, 1)

def simulated_annealing():
    x = random.uniform(-10, 10)
    T = 100
    cooling = 0.95

    while T > 0.001:
        new_x = neighbor(x)

        delta = f(new_x) - f(x)

        if delta > 0:
            x = new_x
        else:
            prob = math.exp(delta / T)
            if random.random() < prob:
                x = new_x

        T *= cooling

    return x, f(x)

solution, value = simulated_annealing()
print("Best solution:", solution)
print("Best value:", value)