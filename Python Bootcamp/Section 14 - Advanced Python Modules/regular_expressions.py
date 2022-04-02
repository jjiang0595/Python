import re

text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)
pattern = 'phone'
print(re.search(pattern, text))
pattern = 'NOT IN TEXT'
print(re.search(pattern, text))
pattern = 'phone'
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())
text = 'my phone once, my phone twice'
match = re.search(pattern, text)
print(match)
matches = re.findall('phone', text)
print(matches)
for i in re.finditer('phone', text):
    print(i)
    