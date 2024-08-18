import numpy as np

# Activation function (ReLU)
# Activation function (ReLU) for scalar or array inputs
def relu(x):
    return np.maximum(0, x)

# Derivative of ReLU
def relu_derivative(x):
    return (x > 0).astype(int)

# Define a simple neural network class
class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_hidden = np.zeros(hidden_size)
        self.bias_output = np.zeros(output_size)
        self.learning_rate = learning_rate

    def forward(self, inputs):
        self.hidden_layer = relu(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        self.output_layer = np.dot(self.hidden_layer, self.weights_hidden_output) + self.bias_output
        return self.output_layer

    def backward(self, inputs, targets):
        output_error = self.output_layer - targets
        output_delta = output_error
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * relu_derivative(self.hidden_layer)

        self.weights_hidden_output -= self.learning_rate * np.dot(self.hidden_layer.T, output_delta)
        self.weights_input_hidden -= self.learning_rate * np.dot(inputs.T, hidden_delta)
        self.bias_output -= self.learning_rate * np.sum(output_delta, axis=0)
        self.bias_hidden -= self.learning_rate * np.sum(hidden_delta, axis=0)

    def train(self, inputs, targets, epochs):
        for epoch in range(epochs):
            self.forward(inputs)
            self.backward(inputs, targets)


# Generate training data for addition
X_train = np.random.randint(1, 100000000000, (0, 2))
y_train = np.sum(X_train, axis=1).reshape(-1, 1)

# Initialize and train the neural network
input_size = 2
hidden_size = 64
output_size = 1
learning_rate = 0.001

nn = SimpleNN(input_size, hidden_size, output_size, learning_rate)
nn.train(X_train, y_train, epochs=10)

# Test the trained model
X_test = np.random.randint(1, 1000000000, (10, 2))
predictions = nn.forward(X_test)

print("Predictions:", predictions[:10])  # Displaying first 10 predictions
