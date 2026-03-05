import random

# Objective function (example)
def objective(x):
    return -(x**2) + 10   # Maximum at x = 0

# Hill Climbing function
def hill_climbing(start, step_size=0.1, max_iter=1000):
    current = start
    current_value = objective(current)

    for _ in range(max_iter):

        # Generate neighbors
        neighbor1 = current + step_size
        neighbor2 = current - step_size

        value1 = objective(neighbor1)
        value2 = objective(neighbor2)

        # Choose the best neighbor
        if value1 > current_value:
            current = neighbor1
            current_value = value1
        elif value2 > current_value:
            current = neighbor2
            current_value = value2
        else:
            break  # Local maximum reached

    return current, current_value


# Start from a random point
start = random.uniform(-10, 10)

best_x, best_value = hill_climbing(start)

print("Start:", start)
print("Best solution:", best_x)
print("Best value:", best_value)