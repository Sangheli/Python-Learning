import numpy as np


# sigmoid function
def sigmoid(x):
	return 1 / (1 + np.exp(-x))


def sigmoid2(x):
	# print("----------")
	# print(np.tanh(x))
	return np.tanh(x)


def sigmoid_derivative(x):
	# computing derivative to the Sigmoid function
	return x * (1 - x)


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset            
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
synapse0 = 2 * np.random.random((3, 1)) - 1


def predict(x):
	# return sigmoid2(np.dot(x, synapse0))
	return sigmoid(np.dot(x, synapse0))


for iter in range(10000):
	# forward propagation
	l0 = X
	l1 = predict(l0)
	l1_error = y - l1

	# multiply how much we missed by the
	# slope of the sigmoid at the values in l1
	l1_delta = l1_error * sigmoid_derivative(l1)

	# update weights
	synapse0 += np.dot(l0.T, l1_delta)

X2 = np.array([[0, 0, 1],
               [1, 1, 1]])

print("Output After Training:")
print(predict(X2))
