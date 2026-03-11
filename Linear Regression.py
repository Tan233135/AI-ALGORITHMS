# Sample dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Parameters
m = 0   # slope
b = 0   # intercept
lr = 0.01   # learning rate
epochs = 1000

n = len(x)

# Training using Gradient Descent
for _ in range(epochs):
    
    dm = 0
    db = 0
    
    for i in range(n):
        y_pred = m * x[i] + b
        error = y_pred - y[i]
        
        dm += error * x[i]
        db += error
    
    m -= lr * (2/n) * dm
    b -= lr * (2/n) * db

print("Slope (m):", m)
print("Intercept (b):", b)

# Prediction
def predict(x):
    return m * x + b

print("Prediction for x=6:", predict(6))