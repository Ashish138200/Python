import numpy as np
my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(int(input("Element:")))
my_array = np.array(my_array)
print(np.ceil(my_array))
my_array1 = []
b = int(input("Size of array:"))
for i in range(b):
    my_array1.append(int(input("Element:")))
my_array1 = np.array(my_array1)
print(np.ceil(my_array1))
print(my_array+my_array1)