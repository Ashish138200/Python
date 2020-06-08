import numpy as np

a = np.array([(1, 2, 3), (2, 3, 3)])
b=np.array([(1,3,1),(1,3,1)])
print(a)
print(a.ndim)  # for checking dimension
print(a.itemsize)  # byte of each element
print(a.dtype)  # data type
print(a.size)  # size of an array
print(a.shape)  # shape of an array
a = a.reshape(3 , 2)# reshape
print(a)
print(a[0:,1]) # slicing
a=np.linspace(1,2,3) # line spacing
print(a)
print()
b=np.array([(1,3,1),(1,3,1)])
print(b.min())
print(b.max())
print(b.sum())
print()
print(a.sum(axis=0))
print(np.sqrt(a))
print(np.std(a))
#matrix add,,sub,muk

print()
print(a+b)

#concatination

print(np.hstack((a,b)))

print(a.ravel())