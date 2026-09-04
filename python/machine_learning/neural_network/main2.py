import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np

model = Sequential([
    Input(shape=(2,)), # Define input shape using an Input layer
    Dense(units=3, activation='sigmoid'),
    Dense(units=1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x, y, epochs=10)
model.predict(np.array([[12, 5]]))
# neural network using library