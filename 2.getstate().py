#The getstate() method returns an object 
#with the current state of the random number generator.
'''import random
print(random.getstate())
'''

import random
# remember this state
state = random.getstate()
# print 10 random numbers
print(random.sample(range(20), k = 10))
# restore state
random.setstate(state)
# print same first 5 random numbers
# as above
print(random.sample(range(20), k = 5))
