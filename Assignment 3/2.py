'''
Neural Network Deep Learning
ICP 3
author: Sreeja Madhagoni
student ID: 700755861
email: sxm58610@ucmo.edu

2. Numpy
Using NumPy create random vector of size 20 having only float in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)
(you can NOT implement it via for loop)
'''
import numpy as np

# Create a random vector of size 20 with float values between 1 and 20
vec = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
vec = vec.reshape(4, 5)
print(vec)
# Replace the max value in each row with 0 (axis=1)
vec[np.arange(4), vec.argmax(axis=1)] = 0

print(vec)
