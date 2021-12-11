import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.losses import BinaryCrossentropy

(x_train, y_train), (x_val, y_val) = mnist.load_data()

print(x_train)

x_train = x_train.astype('float32') / 255
y_train = to_categorical(y_train)

