import time, timeit


def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))


def func_two(n):
    return list(map(str, range(n)))


print(func_two(10))

#CURRENT TIME BEFORE
start_time = time.time()
# RUN CODE
result = func_two(10)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

print(elapsed_time)

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=1000000))

stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=1000000))
