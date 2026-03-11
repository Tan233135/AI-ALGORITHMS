# Simple dataset
data = [
    {"age": 22, "income": 20000, "buy": "No"},
    {"age": 25, "income": 25000, "buy": "No"},
    {"age": 35, "income": 50000, "buy": "Yes"},
    {"age": 45, "income": 60000, "buy": "Yes"},
]

# Simple decision rule
def decision_tree(age, income):
    if age < 30:
        return "No"
    else:
        if income > 40000:
            return "Yes"
        else:
            return "No"

# Prediction
print(decision_tree(40, 55000))