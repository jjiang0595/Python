import math, random
import pdb

value = 4.35
value = math.floor(value)
print(value)
value = 4.35
value = math.ceil(value)
print(value)
print(round(6.5))
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.radians(180))

print(random.randint(0, 100))
random.seed(101)
print(random.randint(0, 100))

mylist = list(range(0, 20))
print(mylist)
print(random.choice(mylist))
# SAMPLE WITH REPLACEMENT
print(random.choices(population=mylist, k=10))
# SAMPLE WITHOUT REPLACEMENTS
print(random.sample(population=mylist, k=10))
print(mylist)
random.shuffle(mylist)
print(mylist)
print(random.uniform(0, 100))
