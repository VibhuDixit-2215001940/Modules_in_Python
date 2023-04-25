#1.seed()-->
    #The seed() method is used to initialize the random number generator. 
    #The random number generator needs a number to start with (a seed value).

import random
random.seed(10)
print(random.random())


import random
random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

import random       # random module is imported
for i in range(5):
	random.seed(0)          # Any number can be used in place of '0'
    print(random.randint(1,1000))      	# Generated random number will be between 1 to 1000
	
