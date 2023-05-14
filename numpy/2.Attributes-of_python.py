from numpy import *
#ndim
a=array([1,2,3,4])
print(a.ndim)       #1

#shape--> return no. of elements of array in tuple format
a=array([1,2,3,4])
print(a.shape)      #(4,)

#reshape
a=array([1,2,3,4])
print(a.reshape(2,2))       #[[1 2] [3 4]]

#flatten
a=array([[1,2],[3,4]])
b=a.flatten()
print(b)        #[1 2 3 4]

#eye-->form a matrix with 1 as diagonal elements
a=eye(2,2)
print(a)     #   [[1. 0.]
              #      [0. 1.]]


