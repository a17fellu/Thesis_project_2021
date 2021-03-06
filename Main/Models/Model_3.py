# Imports should be grouped in the following order:
#
# Standard library imports.
# Related third party imports.
# Local application/library specific imports.
# You should put a blank line between each group of imports.
# https://www.python.org/dev/peps/pep-0008/#imports

# System imports
import os
import random as rn
import shutil
from datetime import datetime

# 3rd party imports
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.models import Sequential


""" Class comment

Bla bla bla bla bla
"""


class Model_3:
    def __init__(self, random_seed):
        self.author = "Ryssinspirerad"
        self.name = self.__class__.__name__
        self.description = "Ryssinspirerad"
        self.seed = random_seed

        # Setting up seed for repeatability
        # More info on https://github.com/NVIDIA/tensorflow-determinism
        os.environ['TF_DETERMINISTIC_OPS'] = '1'
        rn.seed(self.seed)
        np.random.seed(self.seed)
        tf.random.set_seed(self.seed)

        self.timestamp = self.get_timestamp()
        self.epochs = 15
        self.batch_size = 128
        self.verbose = 1

        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu', input_shape=(32, 32, 3)))
        self.model.add(MaxPool2D(pool_size=2))
        self.model.add(Flatten())
        self.model.add(Dense(500, activation='relu'))
        self.model.add(Dense(43, activation='softmax'))
        self.optimizer = tf.keras.optimizers.SGD(lr=0.005, momentum=0.5)
        self.model.compile(optimizer=self.optimizer, loss='categorical_crossentropy', metrics=["accuracy"])

    def get_name_with_timestamp(self, serial):
        return self.name + "_S" + str(serial) + "_" + self.timestamp

    def get_timestamp(self):
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        return str(formatted_timestamp)

    def copy_model_file(self, serial, file_path):
        shutil.copy2("Models/" + self.name + ".py", file_path + self.get_name_with_timestamp(serial) + ".py")

    def get_variables(self):
        return self.model.optimizer.__dict__, self.batch_size, self.seed
