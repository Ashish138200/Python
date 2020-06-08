import numpy as np
import time
import sys

# less memory size
S = range(1000)
print(sys.getsizeof(5) * len(S))
D = np.arange(1000)
print(D.size * D.itemsize)
# less time
SIZE = 100000
l1 = range(SIZE)
l2 = range(SIZE)
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)
start = time.time()
res = [(x, y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000)
start = time.time()
res = a1 + a2
print((time.time() - start) * 1000)
