# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
# lambda and map functions.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


my_list = [1,2,3,4,5,6,7,8,9,10]

squared_list = list(map(lambda x : x**2 , my_list))

print(squared_list)