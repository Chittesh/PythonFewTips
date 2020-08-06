import random
# this return a vlaue between 0 and 1
print(random.random())
#if we want to generate an integer between 2 integers
print(random.randint(1,10))
#if we want to add interval
print(random.randrange(1,25,2))
#muliple of 3
print(random.randrange(0,25,3))

#random.choice
list_values = [2,3,4,5,2,1]
print(random.choice(list_values))
#to get 2 random values sample
print(random.sample(list_values,2))
