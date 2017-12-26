# Simple example using recurrent neural network to predict time series values

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.normalization import batch_normalization
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

step_radians = 0.01
steps_of_history = 200
steps_in_future = 1
index = 0

x = np.sin(np.arange(0, 20*math.pi, step_radians))

seq = []
next_val = []

for i in range(0, len(x) - steps_of_history, steps_in_future):
    seq.append(x[i: i + steps_of_history])
    next_val.append(x[i + steps_of_history])

seq = np.reshape(seq, [-1, steps_of_history, 1])
next_val = np.reshape(next_val, [-1, 1])
print(np.shape(seq))

trainX = np.array(seq)
trainY = np.array(next_val)

# Network building
net = tflearn.input_data(shape=[None, steps_of_history, 1])
net = tflearn.simple_rnn(net, n_units=32, return_seq=False)
net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer='sgd', loss='mean_square', learning_rate=0.1)

# Training
model = tflearn.DNN(net, clip_gradients=0.0, tensorboard_verbose=0)
model.fit(trainX, trainY, n_epoch=15, validation_set=0.1, batch_size=128)

# Testing
x = np.sin(np.arange(20*math.pi, 24*math.pi, step_radians))

seq = []

for i in range(0, len(x) - steps_of_history, steps_in_future):
    seq.append(x[i: i + steps_of_history])

seq = np.reshape(seq, [-1, steps_of_history, 1])
testX = np.array(seq)

# Predict the future values
predictY = model.predict(testX)
print(predictY)

# Plot the results
plt.figure(figsize=(20,4))
plt.suptitle('Prediction')
plt.title('History='+str(steps_of_history)+', Future='+str(steps_in_future))
plt.plot(x, 'r-', label='Actual')
plt.plot(predictY, 'gx', label='Predicted')
plt.legend()
plt.savefig('sine.png')