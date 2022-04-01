from collections import Counter, defaultdict, namedtuple

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]

print(Counter(mylist))

mylist = ['a','a',10,10,10]
print(Counter(mylist))

mylist = Counter('aaaabbbbsgsgsjs')
print(Counter(mylist))

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))

letters = 'aaabbbbccccccddddddddddd'
c = Counter(letters)
list(c)

d = {'a': 10}
print(d)
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['WRONG KEY!'])

mytuple = (10, 20, 30)
print(mytuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name="Sam")
print(sammy.age)
