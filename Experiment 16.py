import random
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Input data (4 samples, 2 features)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Output data (targets)
y = [0, 1, 1, 0]

# Initialize weights randomly
input_layer_neurons = 2  # input layer (2 features)
hidden_layer_neurons = 2  # hidden layer
output_neurons = 1  # output layer

# Random weights
wh = [[random.uniform(-1, 1) for _ in range(hidden_layer_neurons)] for _ in range(input_layer_neurons)]
bh = [random.uniform(-1, 1) for _ in range(hidden_layer_neurons)]

wo = [[random.uniform(-1, 1)] for _ in range(hidden_layer_neurons)]
bo = random.uniform(-1, 1)

# Learning rate
lr = 0.5

# Training loop
for epoch in range(10000):
    for i in range(len(X)):
        # Forward pass
        hidden_input = [0] * hidden_layer_neurons
        for j in range(hidden_layer_neurons):
            hidden_input[j] = sum([X[i][k] * wh[k][j] for k in range(input_layer_neurons)]) + bh[j]
        hidden_output = [sigmoid(h) for h in hidden_input]

        final_input = sum([hidden_output[j] * wo[j][0] for j in range(hidden_layer_neurons)]) + bo
        final_output = sigmoid(final_input)

        # Calculate error
        error = y[i] - final_output

        # Backpropagation
        d_output = error * sigmoid_derivative(final_output)

        d_hidden = [0] * hidden_layer_neurons
        for j in range(hidden_layer_neurons):
            d_hidden[j] = d_output * wo[j][0] * sigmoid_derivative(hidden_output[j])

        # Update output weights and bias
        for j in range(hidden_layer_neurons):
            wo[j][0] += hidden_output[j] * d_output * lr
        bo += d_output * lr

        # Update hidden weights and bias
        for j in range(hidden_layer_neurons):
            for k in range(input_layer_neurons):
                wh[k][j] += X[i][k] * d_hidden[j] * lr
            bh[j] += d_hidden[j] * lr

# Test after training
print("Final output after training:")
for i in range(len(X)):
    hidden_input = [sum([X[i][k] * wh[k][j] for k in range(input_layer_neurons)]) + bh[j] for j in range(hidden_layer_neurons)]
    hidden_output = [sigmoid(h) for h in hidden_input]
    final_input = sum([hidden_output[j] * wo[j][0] for j in range(hidden_layer_neurons)]) + bo
    final_output = sigmoid(final_input)
    print(f"Input: {X[i]}, Predicted Output: {final_output:.3f}")
