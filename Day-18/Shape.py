import numpy as np

data = np.array(
    [[77, 54, 89],
     [84, 48, 85],
     [72, 28, 74]
     ]
)

print(data)
print(data.shape)
print(data.ndim)

print(data[0])      
print(data[:, 0])   
print(data[1, 2])   

sub = data[:2, :2]
print(sub)

#sub[:] = 0
print(data)

print(np.sum(data))
print(np.sum(data, axis = 0))
print(np.sum(data, axis = 1))