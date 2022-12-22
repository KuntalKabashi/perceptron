import numpy as np

# define Unit Step Function
def unitStep(v):
	if v >= 1:
		return 1
	else:
		return -1

# design Perceptron Model
def perceptronModel(x, w, b):
	v = np.dot(w, x) + b
	y = unitStep(v)
	return y

# AND Logic Function
# w1 = -1, w2 = -1, b = 1
def AND_logicFunction(x):
	w = np.array([-1, -1])
	b = 1
	return perceptronModel(x, w, b)

# testing the Perceptron Model
test1 = np.array([-1, 1])
test2 = np.array([1, 1])
test3 = np.array([-1, -1])
test4 = np.array([1, -1])

print("NAND({}, {}) = {}".format(-1, 1, AND_logicFunction(test1)))
print("NAND({}, {}) = {}".format(1, 1, AND_logicFunction(test2)))
print("NAND({}, {}) = {}".format(-1, -1, AND_logicFunction(test3)))
print("NAND({}, {}) = {}".format(1, -1, AND_logicFunction(test4)))