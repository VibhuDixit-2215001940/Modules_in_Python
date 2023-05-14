from numpy import *
a=array([1,2,3,4])
print(a)        #[1 2 3 4]

#Using linspace
a=linspace(1,10,5)
print(a)        #[ 1.    3.25  5.5   7.75 10.  ]

#Using logspace()
a=logspace(1,10,5)
print(a)        #[1.00000000e+01 1.77827941e+03 3.16227766e+05 5.62341325e+07 1.00000000e+10]

#Using arange
a=arange(1,10,5)
print(a)    #[1 6]

#Using zeros() and ones()
a=zeros(3)     #Default type--> int
print(a)

b=ones(3,float)
print(b)
