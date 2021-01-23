#Random Floating Point Values
from random import seed
from random import random

seed(1)
print(random())

# reset the seed
seed(1)
# generate some random numbers
print(random())

min = 1
max = 10
scaled_value = min + (random()* (max - min))*10
print(scaled_value)

# Random Integer Values
from random import randint
from random import seed

seed(1)
print(randint(0, 10))

# Random Gaussian Values
from random import seed
from random import gauss
seed(1)
print(gauss(0, 1))

# Randomly Choosing From a List
from random import seed
from random import choice

seed(1)
sequence = [i for i in range(20)]
print(sequence)
selection = choice(sequence)
print(selection)

# Random Subsample From a List
from random import seed
from random import sample

seed(1)
sequence = [i for i in range(20)]
print(sequence)
subset = sample(sequence, 5)
print(subset)

# Randomly Shuffle a Sequence
from random import seed
from random import shuffle

seed(1)
sequence = [i for i in range(20)]
print(sequence)
shuffle(sequence)
print(sequence)

# References.txt
# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/