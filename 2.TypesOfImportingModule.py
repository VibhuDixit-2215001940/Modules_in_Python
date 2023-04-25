# 1. Importing as a whole module
from random import *
n=randint(5,10)     #Can directly access the f() in module
print(n)

# 2. Imoprting only module
import random 
n=random.randint(5,10)      #First we have to provide module name & then f() to be used
print(n)

# 3. Importing only f()  of that module
from random import randint as r
n=r(5,10)
print(n)

