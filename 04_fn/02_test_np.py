import numpy as np
import matplotlib.pyplot as plt

count = 3

seq = np.ones((count, count, 4), dtype=np.int8)
for i in seq:
    for j in i:
        print(j[1])

