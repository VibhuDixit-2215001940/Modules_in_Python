from numpy import *

#diag
a=diag([1,5,6,7])
print(a)            #[[1 0 0 0]
                    #[0 5 0 0]
                    #[0 0 6 0]
                    #[0 0 0 7]]
#randint
a=random.randint(1,10,5)
print(a)        #[3 7 4 8 8]

#rand-->default value is float
a=random.rand(5)
print(a)        #[0.22779896 0.59692973 0.85001046 0.0372333  0.42476684]

#randn-->return negative float type value
a=random.randn(5)
print(a)        #[-0.05858925 -1.07172729 -1.04126692  2.33112654 -0.12818845]

#sum
a=array([1,2,3,4])      #sum(axis=0)-->columns sum(axis=1)-->rows
print(sum(a))       #10

#argmin-->return index of min element
a=array([1,2,3,4])
print(a.argmin())       #0

#mean
a=array([1,2,3,4])
print(a.mean())     #2.5

#transpose
a=array([[1,2],[3,4]])
print(a.transpose())        #[[1 3]
                            #[2 4]]