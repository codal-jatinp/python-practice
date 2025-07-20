# from math import inf

# user = dict({ 'id': 1, 'name': 'jatin' })

# print(list(user)) # Prints keys

# print('Number of items', len(user))

# # print(user['salary']) # Will raise KeyError

# class SalariedUser(dict):
#   def __missing__(self, key):
#     return 0

# emp = SalariedUser(user)

# emp['salary'] += 5

# del emp['name']

# print(emp, *iter(emp))

# print(dict.fromkeys(['id', 'name', 'salary'], None).items())

# print(emp.pop('joining_date', inf))

# emp.setdefault('joiningDate', inf)

# print(emp)

# emp.popitem() # LIFO pop

# print({ 'name': 'jatin', 'id': 1 } | { 'name': 'putin' })
# print({ 'name': 'putin' } | { 'name': 'jatin', 'id': 10 })

first = { 'name': 'jatin', 'company': 'Greates One Ever' }
# second = { 'id': 1, 'name': 'putin' }

first |= [('name', 'putin')]

print(first)
