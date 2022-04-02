import re

text = 'My phone number is 408-555-1234'
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phone_pattern)
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(3))
