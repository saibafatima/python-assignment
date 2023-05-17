# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
# ['python', 'php', 'aba', 'radar', 'level']

my_list = ['python', 'php', 'aba', 'radar', 'level']

palindrome_list = list(filter(lambda x : x== x[::-1], my_list))

print(palindrome_list)