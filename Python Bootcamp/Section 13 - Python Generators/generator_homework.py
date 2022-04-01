import random

# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def gensquares(n):
    for number in range(n):
        yield number**2


for x in gensquares(10):
    print(x)

print("-----------------------------------------------")

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
print("-----------------------------------------------")

# Problem 3
# Use the iter() function to convert the string below into an iterator:
s = 'hello'

s = iter(s)
print("-----------------------------------------------")

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a
# return statement.

# A generator using a yield statement would use less memory and would
# only give out one output at a time compared to a normal function with a return function.


# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
#
# my_list = [1,2,3,4,5]
#
# gencomp = (item for item in my_list if item > 3)
#
# for item in gencomp:
#     print(item)
# 4
# 5
# Hint: Google generator comprehension!

# In this context, gencomp would mean that for each item in the list and if the item is greater than 3, then set gencomp to item.

