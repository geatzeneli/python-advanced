import numpy as np

array_2D= np.array([
    [1,2,3,4,5],
    [6,7,8,9, 10]
    ]
)
print(array_2D)

elementi = array_2D[0][2]
print(elementi)

print(array_2D[1][4])

dim = array_2D.ndim
print(dim)

shape = array_2D.shape
print(shape)

madhesia = array_2D.size
print(madhesia)

sub_array = array_2D[:2, :2]
print(sub_array)






