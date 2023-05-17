# Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.

from functools import reduce

my_list = list(range(1,26))

product = reduce(lambda x,y : x*y , my_list)

print(product)